---
title: TalkGlobe (Gradio UI)
emoji: 🗣️
colorFrom: purple
colorTo: red
sdk: gradio
sdk_version: 5.26.0
app_file: src/app.py
pinned: false
license: mit
short_description: Real-time translator with multilang support (Gradio UI)
tags: [webrtc, gradio]
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# TalkGlobe: Real-Time Speech Translation

TalkGlobe is an AI-powered application that enables seamless, real-time speech-to-speech translation. Using the state-of-the-art Seamless-M4T-v2 model from Meta, it delivers:

- **🎙️ 101 input languages** for speech recognition

- **🔊 35 output languages** for natural-sounding translated speech

- **⚡ Instant translation** with low latency

- **🖥️ Intuitive interface** for effortless language selection

Simply speak in your native language, choose a target language, and TalkGlobe generates the translated audio in real time. Ideal for travel, business, or multilingual conversations.

## Supported Languages:

Listed below, are the languages supported (either as source or target) by TalkGlobe (according to facebook/seamless-m4t-v2-large model card).

| code     | language               | Source | Target |
| -------- | ---------------------- | :----: | :----: |
| afr      | Afrikaans              |   ✅   |   ❌   |
| amh      | Amharic                |   ✅   |   ❌   |
| arb      | Modern Standard Arabic |   ✅   |   ✅   |
| ary      | Moroccan Arabic        |   ✅   |   ❌   |
| arz      | Egyptian Arabic        |   ✅   |   ❌   |
| asm      | Assamese               |   ✅   |   ❌   |
| ast      | Asturian               |   ✅   |   ❌   |
| azj      | North Azerbaijani      |   ✅   |   ❌   |
| bel      | Belarusian             |   ✅   |   ❌   |
| ben      | Bengali                |   ✅   |   ✅   |
| bos      | Bosnian                |   ✅   |   ❌   |
| bul      | Bulgarian              |   ✅   |   ❌   |
| cat      | Catalan                |   ✅   |   ✅   |
| ceb      | Cebuano                |   ✅   |   ❌   |
| ces      | Czech                  |   ✅   |   ✅   |
| ckb      | Central Kurdish        |   ✅   |   ❌   |
| cmn      | Mandarin Chinese       |   ✅   |   ✅   |
| cmn_Hant | Mandarin Chinese       |   ✅   |   ✅   |
| cym      | Welsh                  |   ✅   |   ✅   |
| dan      | Danish                 |   ✅   |   ✅   |
| deu      | German                 |   ✅   |   ✅   |
| ell      | Greek                  |   ✅   |   ❌   |
| eng      | English                |   ✅   |   ✅   |
| est      | Estonian               |   ✅   |   ✅   |
| eus      | Basque                 |   ✅   |   ❌   |
| fin      | Finnish                |   ✅   |   ✅   |
| fra      | French                 |   ✅   |   ✅   |
| fuv      | Nigerian Fulfulde      |   ✅   |   ❌   |
| gaz      | West Central Oromo     |   ✅   |   ❌   |
| gle      | Irish                  |   ✅   |   ❌   |
| glg      | Galician               |   ✅   |   ❌   |
| guj      | Gujarati               |   ✅   |   ❌   |
| heb      | Hebrew                 |   ✅   |   ❌   |
| hin      | Hindi                  |   ✅   |   ✅   |
| hrv      | Croatian               |   ✅   |   ❌   |
| hun      | Hungarian              |   ✅   |   ❌   |
| hye      | Armenian               |   ✅   |   ❌   |
| ibo      | Igbo                   |   ✅   |   ❌   |
| ind      | Indonesian             |   ✅   |   ✅   |
| isl      | Icelandic              |   ✅   |   ❌   |
| ita      | Italian                |   ✅   |   ✅   |
| jav      | Javanese               |   ✅   |   ❌   |
| jpn      | Japanese               |   ✅   |   ✅   |
| kam      | Kamba                  |   ✅   |   ❌   |
| kan      | Kannada                |   ✅   |   ❌   |
| kat      | Georgian               |   ✅   |   ❌   |
| kaz      | Kazakh                 |   ✅   |   ❌   |
| kea      | Kabuverdianu           |   ✅   |   ❌   |
| khk      | Halh Mongolian         |   ✅   |   ❌   |
| khm      | Khmer                  |   ✅   |   ❌   |
| kir      | Kyrgyz                 |   ✅   |   ❌   |
| kor      | Korean                 |   ✅   |   ✅   |
| lao      | Lao                    |   ✅   |   ❌   |
| lit      | Lithuanian             |   ✅   |   ❌   |
| ltz      | Luxembourgish          |   ✅   |   ❌   |
| lug      | Ganda                  |   ✅   |   ❌   |
| luo      | Luo                    |   ✅   |   ❌   |
| lvs      | Standard Latvian       |   ✅   |   ❌   |
| mai      | Maithili               |   ✅   |   ❌   |
| mal      | Malayalam              |   ✅   |   ❌   |
| mar      | Marathi                |   ✅   |   ❌   |
| mkd      | Macedonian             |   ✅   |   ❌   |
| mlt      | Maltese                |   ✅   |   ✅   |
| mni      | Meitei                 |   ✅   |   ❌   |
| mya      | Burmese                |   ✅   |   ❌   |
| nld      | Dutch                  |   ✅   |   ✅   |
| nno      | Norwegian Nynorsk      |   ✅   |   ❌   |
| nob      | Norwegian Bokmål       |   ✅   |   ❌   |
| npi      | Nepali                 |   ✅   |   ❌   |
| nya      | Nyanja                 |   ✅   |   ❌   |
| oci      | Occitan                |   ✅   |   ❌   |
| ory      | Odia                   |   ✅   |   ❌   |
| pan      | Punjabi                |   ✅   |   ❌   |
| pbt      | Southern Pashto        |   ✅   |   ❌   |
| pes      | Western Persian        |   ✅   |   ✅   |
| pol      | Polish                 |   ✅   |   ✅   |
| por      | Portuguese             |   ✅   |   ✅   |
| ron      | Romanian               |   ✅   |   ✅   |
| rus      | Russian                |   ✅   |   ✅   |
| slk      | Slovak                 |   ✅   |   ✅   |
| slv      | Slovenian              |   ✅   |   ❌   |
| sna      | Shona                  |   ✅   |   ❌   |
| snd      | Sindhi                 |   ✅   |   ❌   |
| som      | Somali                 |   ✅   |   ❌   |
| spa      | Spanish                |   ✅   |   ✅   |
| srp      | Serbian                |   ✅   |   ❌   |
| swe      | Swedish                |   ✅   |   ✅   |
| swh      | Swahili                |   ✅   |   ✅   |
| tam      | Tamil                  |   ✅   |   ❌   |
| tel      | Telugu                 |   ✅   |   ✅   |
| tgk      | Tajik                  |   ✅   |   ❌   |
| tgl      | Tagalog                |   ✅   |   ✅   |
| tha      | Thai                   |   ✅   |   ✅   |
| tur      | Turkish                |   ✅   |   ✅   |
| ukr      | Ukrainian              |   ✅   |   ✅   |
| urd      | Urdu                   |   ✅   |   ✅   |
| uzn      | Northern Uzbek         |   ✅   |   ✅   |
| vie      | Vietnamese             |   ✅   |   ✅   |
| xho      | Xhosa                  |   ✅   |   ❌   |
| yor      | Yoruba                 |   ✅   |   ❌   |
| yue      | Cantonese              |   ✅   |   ❌   |
| zlm      | Colloquial Malay       |   ✅   |   ❌   |
| zul      | Zulu                   |   ✅   |   ❌   |

## Getting Started

This guide provides step-by-step instructions to set up and run the project on your local machine for development and testing purposes. For details on deploying the project to a production environment, refer to the Deployment section.

### Prerequisites

To set up and run this project, ensure the following software and tools are installed on your system:

- **Python**: Version `3.10.12` or higher is required. Verify your Python version by running:

  ```bash
  python3 --version
  ```

- **Dependencies**: Install the required Python packages listed in requirements.txt using pip. Run the following command in your terminal:

  ```bash
  pip install -r requirements.txt
  ```

### Local Development and Testing

To run the application locally for development and testing purposes, execute the following command in your terminal:

```bash
python app.py
```

> [!WARNING]
> Ensure you are in the project's **src** directory before running the script or adapt running path.

## Deployment

### Deployment on Hugging Face Spaces

To deploy the project on Hugging Face Spaces, follow these steps:

1. Create an account on [Hugging Face](https://huggingface.co) if you don’t already have one.

2. Refer to the official [Spaces Overview](https://huggingface.co/docs/hub/en/spaces-overview) documentation for detailed instructions on setting up and deploying your project.

### Deployment on Other Cloud Platforms

For deployment on other cloud or live systems, consult the documentation provided by your chosen service provider. Each platform may have specific requirements and steps for deploying Python-based applications.

## Built With

- [Python 3.10.12](http://www.python.org/) - Developing with the best programming language

## Authors

**Vlasios Dimitriadis** - _Initial work:_ [TalkGlobe](https://huggingface.co/spaces/blasisd/talk-globe)
