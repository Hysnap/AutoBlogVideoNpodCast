# blog_visual_engine

A reusable, open-source Python library for generating
charts, slides, and narration assets for blog posts.

## Philosophy

- Blog text is the source of truth
- Visuals are derived artifacts
- Everything is offline-capable and open-source

## Features

✅ **Offline Text-to-Speech** - Convert text to audio using system TTS (no API keys needed)
- Uses pyttsx3 for cross-platform offline speech synthesis
- Works on Windows (SAPI5), macOS (NSSpeechSynthesizer), and Linux (eSpeak)
- Multiple voice options and customizable speed/volume

## Installation

```bash
pip install -e .
```

## Quick Start

### Convert Blog Post to Audio (Offline)

```bash
# Simple conversion
python blog_to_audio.py examples/minimal_post/post.md

# Custom output and settings
python blog_to_audio.py post.md -o narration.wav --speed 160 --volume 0.8

# List available voices
python blog_to_audio.py post.md --list-voices
```

### Using in Python

```python
from blog_visual_engine.audio.tts import TextToSpeech
from pathlib import Path

# Initialize TTS engine
tts = TextToSpeech(speed=150, volume=0.9)

# List available voices
voices = tts.list_available_voices()
for voice in voices:
    print(f"{voice['name']}: {voice['id']}")

# Convert text to audio file
text = "Hello! This is offline text-to-speech."
output_path = Path("output.wav")
tts.synthesize(text, output_path)

# Batch process multiple segments
segments = ["Segment one", "Segment two", "Segment three"]
audio_files = tts.synthesize_batch(segments, Path("output_dir"))
```

## Examples

- `examples/minimal_post/` - Minimal blog post example
- `examples/tts_demo.py` - Interactive TTS demo
- `blog_to_audio.py` - CLI tool for blog-to-audio conversion

See examples/minimal_post
