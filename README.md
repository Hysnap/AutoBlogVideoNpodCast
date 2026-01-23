# AutoBlogVideoNpodCast

**Convert your blog posts into engaging multimedia content - videos, audio narration, and visual presentations.**

An open-source Python library that automatically transforms Markdown blog posts into multimedia content including video presentations, audio narration, and visual slides. Designed with an offline-first approach and treating blog text as the single source of truth.

## Features

- **High-Quality Text-to-Speech**: Convert blog text to natural-sounding audio narration
  - **Kokoro TTS** (Recommended): Neural TTS with 10 high-quality voices
  - **pyttsx3** (Alternative): System TTS for smaller footprint
  - Cross-platform support (Windows, macOS, Linux)
  - Multiple voice options with customizable speed
  - Batch processing for multiple text segments
  - See [Kokoro Setup Guide](KOKORO_SETUP.md) for installation

- **Visual Generation**: Create compelling visuals from your content
  - Generate bar charts, line charts, and pie charts from data
  - Customizable color themes and styling
  - Export in PNG/JPG formats

- **Slide Creation**: Build professional presentations
  - Multiple layout types (title, content, two-column, image-text)
  - Automated positioning and formatting
  - Export slides as images or video

- **Markdown Parsing**: Full support for blog post structure
  - Extract sections, headings, and content
  - Parse data/metrics for visualization
  - Generate metadata automatically

## Philosophy

- **Blog text is the source of truth** - Your written content drives everything
- **Visuals are derived artifacts** - Charts and slides generated from your content
- **Offline-first and open-source** - No API dependencies, complete local control

## Quick Start

### Installation

```bash
# Navigate to the project directory
cd blog_visual_engine

# Install core dependencies
pip install -r requirements.txt

# Or install as a package
pip install -e .
```

### Convert Blog Post to Audio

```bash
# Basic conversion
python blog_to_audio.py examples/minimal_post/post.md

# With custom settings
python blog_to_audio.py post.md -o narration.wav --speed 160 --volume 0.8

# List available voices
python blog_to_audio.py post.md --list-voices
```

### Using in Python

```python
from blog_visual_engine.audio.kokoro_tts import KokoroTTS
from pathlib import Path

# Initialize Kokoro TTS engine (high quality)
tts = KokoroTTS(voice="af_sarah", speed=1.0)

# Convert text to audio
text = "Hello! This is high-quality text-to-speech."
tts.synthesize(text, Path("output.wav"))

# Batch process multiple segments
segments = ["Segment one", "Segment two", "Segment three"]
audio_files = tts.synthesize_batch(segments, Path("output_dir"))
```

**Alternative - Using pyttsx3 (system TTS)**:
```python
from blog_visual_engine.audio.tts import TextToSpeech

tts = TextToSpeech(speed=150, volume=0.9)
tts.synthesize("Hello", Path("output.wav"))
```

## Project Structure

```
AutoBlogVideoNpodCast/
├── blog_visual_engine/       # Core Python library
│   ├── audio/               # Text-to-speech modules
│   ├── visuals/             # Chart and visual generation
│   ├── slides/              # Presentation creation
│   ├── config/              # Themes and configuration
│   └── utils/               # Utility functions
├── blog_to_video/           # Example project structure
│   ├── source/              # Blog post markdown files
│   ├── audio/               # Generated audio files
│   └── visuals/             # Generated visual assets
├── examples/                # Usage examples and demos
├── REQUIREMENTS.md          # Detailed requirements documentation
├── INSTALLATION.md          # Comprehensive installation guide
└── DEPENDENCIES.md          # Dependency reference
```

## Documentation

- **[Kokoro TTS Setup](KOKORO_SETUP.md)** - Complete Kokoro TTS installation and configuration guide
- [Installation Guide](INSTALLATION.md) - Platform-specific setup instructions
- [Requirements](REQUIREMENTS.md) - Detailed functional and technical requirements
- [Dependencies](DEPENDENCIES.md) - Complete dependency reference
- [Library README](blog_visual_engine/README.md) - Core library documentation

## Requirements

- Python 3.8 or higher
- Platform-specific audio drivers (for system TTS)
- Core dependencies: kokoro-onnx (or pyttsx3), Pillow, pydub

See [KOKORO_SETUP.md](KOKORO_SETUP.md) and [DEPENDENCIES.md](DEPENDENCIES.md) for complete details.

## Development

```bash
# Install with development tools
pip install -r requirements-dev.txt

# Or use optional dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## Examples

- `examples/minimal_post/` - Minimal blog post conversion example
- `examples/tts_demo.py` - Interactive TTS demonstration
- `blog_to_audio.py` - CLI tool for blog-to-audio conversion

## License

MIT License - See [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! This project emphasizes:
- Offline-first capabilities
- Open-source dependencies only
- Blog text as the source of truth
- Cross-platform compatibility
