# youtube-shorts-generator

## Overview

`youtube-shorts-generator` is an automated pipeline that creates engaging YouTube Shorts using AI. The project takes a prompt, generates a script using a large language model (LLM), converts the script to a voiceover, applies the voiceover to a pre-existing video clip, and adds subtitles matching the script.

## Features

- Script generation using LLMs
- Text-to-speech voiceover creation
- Automatic synchronization of voiceover with video
- Subtitle generation and overlay

## Usage

1. **Input a prompt** describing the desired YouTube Short.
2. The LLM generates a script based on the prompt.
3. The script is converted to a voiceover using a text-to-speech engine.
4. The voiceover is applied to a selected video clip.
5. Subtitles are generated from the script and added to the video.

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt` (e.g., OpenAI API, TTS library, moviepy, ffmpeg)

## Setup

```bash
git clone https://github.com/yourusername/youtube-shorts-generator.git
cd youtube-shorts-generator
pip install -r requirements.txt
```

- Add your api keys to `llm_model/`
- Add background clips in `clips` folder

## Running the Project

```bash
python main.py
```

## Output

The final video with voiceover and subtitles will be saved in the `final/` directory.
