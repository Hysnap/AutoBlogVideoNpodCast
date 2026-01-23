# Kokoro TTS Setup Guide

Kokoro TTS is a high-quality, neural text-to-speech system that runs locally on your machine. It offers significantly better voice quality compared to pyttsx3.

## Features

- **High-Quality Neural Voices**: Natural-sounding speech with excellent prosody
- **Multiple Voices**: 10 voices (American/British, Male/Female)
- **Offline Capable**: Works entirely offline after initial model download
- **Fast Generation**: Leverages ONNX Runtime for efficient inference
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

### Option 1: Install via pip (Recommended)

```bash
# Install kokoro-onnx package
pip install kokoro-onnx
```

### Option 2: Install from source

```bash
# Clone the repository
git clone https://github.com/thewh1teagle/kokoro-onnx.git
cd kokoro-onnx

# Install
pip install .
```

## Initial Setup

### Download Voice Models

On first run, Kokoro will automatically download the required voice models (~100-200MB per voice). This is a one-time download.

```bash
# Test installation and trigger model download
kokoro --text "Hello, this is a test" --output test.wav --voice af_sarah
```

### Verify Installation

```bash
# Check Kokoro version
kokoro --version

# List available commands
kokoro --help
```

## Available Voices

| Voice ID      | Name     | Gender | Accent   | Description                 |
| ------------- | -------- | ------ | -------- | --------------------------- |
| `af_sarah`    | Sarah    | Female | American | Clear, professional voice   |
| `af_bella`    | Bella    | Female | American | Warm, friendly voice        |
| `af_nicole`   | Nicole   | Female | American | Energetic voice             |
| `af_sky`      | Sky      | Female | American | Calm, soothing voice        |
| `am_adam`     | Adam     | Male   | American | Professional male voice     |
| `am_michael`  | Michael  | Male   | American | Deep, authoritative voice   |
| `bf_emma`     | Emma     | Female | British  | Classic British accent      |
| `bf_isabella` | Isabella | Female | British  | Refined British voice       |
| `bm_george`   | George   | Male   | British  | Distinguished British voice |
| `bm_lewis`    | Lewis    | Male   | British  | Young British male voice    |

## Usage Examples

### Basic Command Line

```bash
# Basic synthesis
kokoro --text "Hello world" --output hello.wav --voice af_sarah

# With speed adjustment
kokoro --text "Faster speech" --output fast.wav --voice am_adam --speed 1.5

# Longer text
kokoro --text "This is a longer piece of text that will be converted to speech." \
       --output narration.wav --voice bf_emma --speed 1.0
```

### Using in Python

```python
from blog_visual_engine.audio.kokoro_tts import KokoroTTS
from pathlib import Path

# Initialize
tts = KokoroTTS(voice="af_sarah", speed=1.0)

# Generate audio
text = "Hello! This is Kokoro TTS."
output = Path("output.wav")
tts.synthesize(text, output)

# List voices
voices = tts.list_available_voices()
for voice in voices:
    print(f"{voice['id']}: {voice['name']}")

# Batch processing
segments = ["First segment", "Second segment", "Third segment"]
audio_files = tts.synthesize_batch(segments, Path("output_dir"))
```

### Run Demo Scripts

```bash
# Kokoro TTS demo
python blog_visual_engine/examples/kokoro_tts_demo.py
```

## Configuration

### Speed Control

- **Range**: 0.5 to 2.0
- **Default**: 1.0 (normal speed)
- **0.5**: Half speed (slower, clearer)
- **1.5**: 1.5x speed (faster)
- **2.0**: Double speed (very fast)

```python
tts.set_speed(0.8)  # Slightly slower
```

### Voice Selection

```python
# Change voice
tts.set_voice("am_michael")  # Deep male voice
tts.set_voice("bf_emma")     # British female
```

### Sample Rate

- **Default**: 24000 Hz (24 kHz)
- **Options**: 16000, 22050, 24000, 44100
- Higher sample rates = better quality but larger files

```python
tts = KokoroTTS(voice="af_sarah", speed=1.0, sample_rate=44100)
```

## Troubleshooting

### Error: "Kokoro TTS not found"

**Solution**: Install kokoro-onnx

```bash
pip install kokoro-onnx
```

### Error: "Model download failed"

**Solution**: Check internet connection and try manual download

```bash
# The models will be downloaded to:
# Windows: C:\Users\<username>\.cache\kokoro\
# macOS/Linux: ~/.cache/kokoro/

# Retry download
kokoro --text "test" --output test.wav --voice af_sarah
```

### Error: "ONNX Runtime not found"

**Solution**: Install ONNX Runtime

```bash
pip install onnxruntime
# Or for GPU support:
pip install onnxruntime-gpu
```

### Slow Performance

**Solutions**:

1. Use GPU acceleration:

   ```bash
   pip install onnxruntime-gpu
   ```

2. Lower sample rate:

   ```python
   tts = KokoroTTS(sample_rate=16000)  # Faster, smaller files
   ```

3. Ensure models are fully downloaded (first run is always slower)

### Large File Sizes

**Solutions**:

1. Use lower sample rate (16000 Hz instead of 24000 Hz)
2. Compress using pydub after generation:
   ```python
   from pydub import AudioSegment
   audio = AudioSegment.from_wav("output.wav")
   audio.export("compressed.mp3", format="mp3", bitrate="128k")
   ```

## Platform-Specific Notes

### Windows

- Works out of the box after pip install
- Models stored in: `C:\Users\<username>\.cache\kokoro\`
- Recommended: Python 3.9-3.11

### macOS

- May need to install libsndfile:
  ```bash
  brew install libsndfile
  ```
- Models stored in: `~/.cache/kokoro/`

### Linux (Ubuntu/Debian)

- Install required system packages:
  ```bash
  sudo apt-get update
  sudo apt-get install libsndfile1 ffmpeg
  ```
- Models stored in: `~/.cache/kokoro/`

## Comparison: Kokoro vs pyttsx3

| Feature           | Kokoro TTS                   | pyttsx3                     |
| ----------------- | ---------------------------- | --------------------------- |
| Voice Quality     | ⭐⭐⭐⭐⭐ Neural, natural   | ⭐⭐ Robotic, system voices |
| Speed             | Fast (ONNX optimized)        | Fast                        |
| Offline           | ✅ After model download      | ✅ Completely offline       |
| Setup             | Pip install + model download | Pip install only            |
| Voice Options     | 10 curated voices            | System-dependent            |
| File Size         | Larger (neural models)       | Smaller                     |
| Cross-platform    | ✅                           | ✅                          |
| Internet Required | Only for initial download    | ❌ Never                    |

## Resources

- **GitHub Repository**: https://github.com/thewh1teagle/kokoro-onnx
- **PyPI Package**: https://pypi.org/project/kokoro-onnx/
- **ONNX Runtime**: https://onnxruntime.ai/
- **Issue Tracker**: https://github.com/thewh1teagle/kokoro-onnx/issues

## Migration from pyttsx3

If you're switching from pyttsx3 to Kokoro:

```python
# Old pyttsx3 code
from blog_visual_engine.audio.tts import TextToSpeech
tts = TextToSpeech(speed=150, volume=0.9)

# New Kokoro code
from blog_visual_engine.audio.kokoro_tts import KokoroTTS
tts = KokoroTTS(voice="af_sarah", speed=1.0)

# The synthesize and synthesize_batch methods work the same way!
```

**Note**: Speed values differ:

- pyttsx3: Words per minute (100-200 typical)
- Kokoro: Speed multiplier (0.5-2.0, where 1.0 is normal)

## Updates

### Updating Kokoro

```bash
# Update to latest version
pip install --upgrade kokoro-onnx

# Force reinstall if needed
pip install --force-reinstall kokoro-onnx
```

## Support

If you encounter issues:

1. Check this guide first
2. Verify installation: `kokoro --version`
3. Check GitHub issues: https://github.com/thewh1teagle/kokoro-onnx/issues
4. Report bugs with system info and error messages

---

**Last Updated**: January 23, 2026  
**Kokoro Version**: Latest (check with `kokoro --version`)  
**Maintained By**: AutoBlogVideoNpodCast Team
