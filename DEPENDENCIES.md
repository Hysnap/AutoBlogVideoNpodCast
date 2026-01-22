# Python Dependencies Reference - AutoBlogVideoNpodCast

## Summary

AutoBlogVideoNpodCast has **3 core dependencies** and **8 development dependencies**.

### Quick Install

```bash
# Core only
pip install pyttsx3 pillow pydub

# Or from project
pip install -r blog_visual_engine/requirements.txt

# Development (includes core)
pip install -r blog_visual_engine/requirements-dev.txt
```

---

## Core Dependencies (Required)

### 1. pyttsx3 (≥2.90)

**Text-to-Speech Synthesis Engine**

- **What it does**: Converts text to speech audio
- **Why needed**: Core feature for narration generation
- **Installation**: `pip install pyttsx3`
- **Platform support**: Windows, macOS, Linux
- **Offline**: ✅ Yes (no internet required)
- **Key features**:
  - Multiple voices per OS
  - Adjustable speech rate (words per minute)
  - Volume control
  - WAV file output
  - Live speech playback
- **Documentation**: https://pyttsx3.readthedocs.io/

**System Requirements**:

- Windows: Built-in SAPI5 or Microsoft Speech Platform
- macOS: Built-in NSSpeechSynthesizer
- Linux: espeak, festival, or NVDA

**Usage Example**:

```python
from blog_visual_engine.audio.tts import TextToSpeech

tts = TextToSpeech(speed=150, volume=0.9)
tts.synthesize("Hello world", "output.wav")
```

---

### 2. Pillow (≥9.0.0)

**Python Imaging Library**

- **What it does**: Image creation, processing, and manipulation
- **Why needed**: Generate slides, charts, and visual content
- **Installation**: `pip install pillow`
- **Platform support**: Windows, macOS, Linux
- **Key features**:
  - Create and edit images
  - Format conversion (PNG, JPG, JPEG, BMP, etc.)
  - Image filtering and effects
  - Text rendering
  - Image composition and layering
- **Documentation**: https://pillow.readthedocs.io/

**Usage Example**:

```python
from PIL import Image, ImageDraw

img = Image.new('RGB', (800, 600), color='white')
draw = ImageDraw.Draw(img)
draw.text((100, 100), "Hello", fill='black')
img.save('slide.png')
```

---

### 3. pydub (≥0.25.1)

**Audio Processing Library**

- **What it does**: Audio file manipulation and processing
- **Why needed**: Handle audio files, concatenation, and mixing
- **Installation**: `pip install pydub`
- **Platform support**: Windows, macOS, Linux
- **Key features**:
  - Load/save audio in multiple formats (WAV, MP3, OGG, FLAC)
  - Audio concatenation and slicing
  - Volume control
  - Format conversion
  - Audio merging and effects
- **Documentation**: https://github.com/jiaaro/pydub

**Dependencies**: Requires ffmpeg binary (separate installation)

**Install ffmpeg**:

```bash
# Windows (Chocolatey)
choco install ffmpeg

# macOS (Homebrew)
brew install ffmpeg

# Linux (apt)
sudo apt-get install ffmpeg
```

**Usage Example**:

```python
from pydub import AudioSegment

audio = AudioSegment.from_wav("narration.wav")
audio = audio + 3  # Increase volume by 3dB
audio.export("louder.wav", format="wav")
```

---

## Development Dependencies (Optional)

### Testing & Coverage

```bash
pytest>=7.0.0           # Unit testing framework
pytest-cov>=4.0.0       # Code coverage measurement
```

### Code Quality

```bash
black>=22.0.0           # Code formatter (PEP 8)
flake8>=4.0.0           # Code linter (style violations)
mypy>=0.990             # Static type checker
pylint>=2.15.0          # Advanced static analysis
isort>=5.10.0           # Import statement sorter
```

### Documentation

```bash
sphinx>=5.0.0           # Documentation generator
sphinx-rtd-theme>=1.0.0 # ReadTheDocs theme
```

### Utilities

```bash
coverage>=6.0           # Coverage analysis
ipython>=8.0.0          # Interactive Python shell
jupyter>=1.0.0          # Jupyter notebook support
```

---

## Installation Verification

### Test Each Core Dependency

```bash
# Test pyttsx3
python -c "
import pyttsx3
engine = pyttsx3.init()
print(f'✅ pyttsx3 OK - {len(engine.getProperty(\"voices\"))} voices available')
"

# Test Pillow
python -c "
from PIL import Image
img = Image.new('RGB', (100, 100))
print('✅ Pillow OK')
"

# Test pydub
python -c "
from pydub import AudioSegment
print('✅ pydub OK')
"
```

### Full Import Test

```bash
python -c "
from blog_visual_engine.audio.tts import TextToSpeech
from blog_visual_engine.config.theme import Theme
from blog_visual_engine.visuals.charts import ChartGenerator
from blog_visual_engine.slides.impress import Presentation
print('✅ All imports successful')
"
```

---

## Dependency Compatibility

### Python Version

- **Minimum**: Python 3.8
- **Tested**: Python 3.8, 3.9, 3.10, 3.11, 3.12
- **Recommended**: Python 3.10 or 3.11

### Operating Systems

| OS            | Status             | Notes                       |
| ------------- | ------------------ | --------------------------- |
| Windows 10/11 | ✅ Fully Supported | SAPI5 voices built-in       |
| macOS 10.13+  | ✅ Fully Supported | System voices available     |
| Ubuntu 20.04+ | ✅ Fully Supported | Requires espeak or festival |
| Linux (other) | ⚠️ Partial         | May need TTS backend setup  |

---

## Troubleshooting Dependencies

### ImportError: No module named 'pyttsx3'

```bash
# Install/reinstall
pip install pyttsx3

# Verify installation
pip show pyttsx3

# Force reinstall
pip install --force-reinstall pyttsx3
```

### ImportError: No module named 'PIL' (Pillow)

```bash
# Install/reinstall
pip install pillow

# Check installation
python -c "from PIL import Image; print(Image.__version__)"
```

### pydub ImportError + ffmpeg missing

```bash
# Install pydub
pip install pydub

# Install ffmpeg (system package)
# See instructions above for your OS
```

### Version Conflicts

```bash
# Check installed versions
pip list | grep -E "(pyttsx3|pillow|pydub)"

# Upgrade to latest
pip install --upgrade pyttsx3 pillow pydub

# Install specific version
pip install pyttsx3==2.90
```

---

## Virtual Environment Best Practices

### Create and Activate

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate.bat

# Activate (macOS/Linux)
source venv/bin/activate
```

### Install Dependencies

```bash
# Inside activated virtual environment
pip install -r requirements.txt

# Verify isolation
which python  # Should point to venv
```

### Deactivate

```bash
deactivate
```

---

## Dependency Graph

```
blog-visual-engine
├── pyttsx3 (offline TTS)
│   └── pywin32 (Windows only)
│
├── pillow (image processing)
│   └── [No external deps]
│
└── pydub (audio processing)
    └── ffmpeg (system binary, not Python package)

[Development]
├── pytest (testing)
├── black (formatting)
├── flake8 (linting)
├── mypy (type checking)
├── sphinx (documentation)
└── [others]
```

---

## Performance Notes

### Installation Time

- First install: 1-3 minutes (depends on internet speed)
- Subsequent installs: < 30 seconds
- **Slowest part**: pyttsx3 compilation on some systems

### Runtime Performance

- **pyttsx3 init**: 2-5 seconds (audio driver initialization)
- **Pillow image creation**: < 100ms
- **pydub audio processing**: Depends on file size

### Optimization Tips

- Use virtual environment to isolate dependencies
- Cache pyttsx3 engine instance (don't reinitialize repeatedly)
- Process images/audio in batches when possible
- Use appropriate image formats (PNG for lossless, JPG for web)

---

## Updating Dependencies

### Check for Updates

```bash
pip list --outdated
```

### Update All

```bash
pip install -U -r requirements.txt
```

### Update Specific

```bash
pip install -U pyttsx3
```

### Freeze Current State

```bash
pip freeze > requirements-locked.txt
```

---

## Additional Resources

### Official Documentation

- pyttsx3: https://pyttsx3.readthedocs.io/
- Pillow: https://pillow.readthedocs.io/
- pydub: https://github.com/jiaaro/pydub

### Installation Guides

- Full guide: See [INSTALLATION.md](INSTALLATION.md)
- Requirements doc: See [REQUIREMENTS.md](REQUIREMENTS.md)

### Support

- GitHub Issues: https://github.com/Hysnap/AutoBlogVideoNpodCast/issues
- Documentation: Check project README.md

---

**Last Updated**: January 22, 2026  
**Version**: 1.0  
**Maintained By**: AutoBlogVideoNpodCast Team
