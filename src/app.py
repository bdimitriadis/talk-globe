import os

from pathlib import Path

import pandas as pd
import torchaudio
import torch
import numpy as np
import gradio as gr

from dotenv import load_dotenv
from fastrtc import (
    get_cloudflare_turn_credentials_async,
    get_cloudflare_turn_credentials,
    WebRTC,
    ReplyOnPause,
)
from transformers import AutoProcessor, SeamlessM4Tv2Model


load_dotenv(override=True)

parent_dir = Path(__file__).parents[1]
config_path = Path(parent_dir, "configs")

processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large")
default_sampling_rate = 16_000


HF_TOKEN = os.getenv("HF_TOKEN")


async def get_credentials():
    return await get_cloudflare_turn_credentials_async(hf_token=HF_TOKEN)


def translate_audio(
    audio: tuple[int, np.ndarray], tgt_language: str
) -> tuple[int, np.ndarray]:
    """Translate the audio that is captured through the streaming component.
    Source language of the audio has to be one of the supported languages to be successful.

    :param audio: the captured audio
    :type audio: tuple[int, np.ndarray]
    :param tgt_language: the target language for translation
    :type tgt_language: str
    :yield: the tuple containing the sampling rate and the audio array
    :rtype: tuple[int, np.ndarray]
    """
    orig_freq, np_array = audio
    waveform = torch.from_numpy(np_array)
    waveform = waveform.to(torch.float32)
    waveform = waveform / 32768.0  # normalize int16 to [-1, 1]

    audio = torchaudio.functional.resample(
        waveform, orig_freq=orig_freq, new_freq=default_sampling_rate
    )  # must be a 16 kHz waveform array

    audio_inputs = processor(
        audios=audio,
        return_tensors="pt",
        sampling_rate=default_sampling_rate,
    )

    audio_array_from_audio = (
        model.generate(**audio_inputs, tgt_lang=tgt_language)[0].cpu().numpy().squeeze()
    )

    yield (default_sampling_rate, audio_array_from_audio)


# Supported target languages for speech
supported_langs_df = pd.read_excel(Path(config_path, "supported_languages.xlsx"))
supported_speech_langs_df = supported_langs_df[
    supported_langs_df["Target"].str.contains("Sp")
]

# Labels and values for supported speech languages dropdown
supported_speech_langs = list(
    zip(supported_speech_langs_df["language"], supported_speech_langs_df["code"])
)

# Sort by the first element of the tuple (full language name)
supported_speech_langs.sort()

css = """
#componentsContainer {
    width: 70%;
    display: block;
    margin-left: auto;
    margin-right: auto;
}

#langDropdown .container .wrap {
    width: 230px;
}

.audio-container {
    padding-bottom: 2rem !important;
    margin-bottom: 2rem !important;
}

.vspace-sm { margin-bottom: 20px !important; }
.vspace-md { margin-bottom: 40px !important; }
.vspace-lg { margin-bottom: 60px !important; }

.tagline {
    color: #4a5568;
}
.tagline-emphasis {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    color: #718096;
    position: relative;
    display: inline-block;
}
.tagline-emphasis:after {
    content: "";
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #6a11cb, transparent);
}

.gradio-footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    padding: 12px;
    background: var(--background-fill-secondary);
    border-top: 1px solid var(--border-color-primary);
    font-size: 0.9em;
    z-index: 100;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 6px;
}
.gradio-footer a {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    color: var(--link-text-color);
    text-decoration: none;
}

.fastrtc-icon {
    height: 24px;
    width: 24px;
}
"""


with gr.Blocks(
    theme=gr.themes.Glass(),
    css=css,
) as demo:
    gr.HTML(
        """
        <div style='display: flex; align-items: center; justify-content: center; gap: 20px'>
            <div style="background-color: var(--block-background-fill); border-radius: 8px">
                <img src="https://images.icon-icons.com/3975/PNG/512/translation_language_translator_icon_251869.png" style="width: 100px; height: 100px;">
            </div>
            <div>
                <h1>TalkGlobe</h1>
                <p class="tagline">
                    Break language barriers in real-time <span class="globe-icon">🌍</span><br>
                    <span class="tagline-emphasis">no more lost in translation</span> <span class="globe-icon">✨</span>
                </p>
            </div>
        </div>
        """,
        elem_classes="vspace-sm",
    )

    # The main components (translation language dropdown and streaming capture component)
    with gr.Group(elem_id="componentsContainer"):
        with gr.Row(equal_height=True, min_height="11rem"):
            with gr.Column(scale=5, elem_id="langCol"):
                target_lang = gr.Dropdown(
                    choices=supported_speech_langs,
                    value="eng",
                    label="Supported Languages",
                    info="Select one of the supported languages for translation",
                    elem_id="langDropdown",
                )

            with gr.Column(scale=5, elem_id="micCol"):
                audio = WebRTC(
                    modality="audio",
                    mode="send-receive",
                    label="Audio Stream",
                    rtc_configuration=get_credentials,
                    server_rtc_configuration=get_cloudflare_turn_credentials(
                        ttl=360_000
                    ),
                )

                # Trigger on pause
                audio.stream(
                    ReplyOnPause(translate_audio),
                    inputs=[audio, target_lang],
                    outputs=[audio],
                    concurrency_limit=5,
                    time_limit=60,
                )

    # Sticky footer (will stay at bottom on all screen sizes)
    gr.HTML(
        """
        <div class="gradio-footer">
            Powered by 
            <a href="https://gradio.app/" target="_blank">
                Gradio <img class="gradio-icon" src="https://www.gradio.app/_app/immutable/assets/gradio.CHB5adID.svg" alt="GradioIcon" style="height:24px; width:auto;">
            </a>
            • 
            <a href="https://freddyaboulton.github.io/gradio-webrtc/" target="_blank">
                FastRTC <img class="fastrtc-icon" src="https://fastrtc.org/fastrtc_logo.png" alt="FastRTCIcon">
            </a>
        </div>
        """
    )

demo.launch()
