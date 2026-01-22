# Installation Guide - AutoBlogVideoNpodCast

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Platform-specific audio drivers

### Basic Installation

```bash
# Navigate to project directory
cd blog_visual_engine

# Install core dependencies
pip install -r requirements.txt

# Or install from source with dependencies
pip install -e .
```

### Development Installation

```bash
cd blog_visual_engine

# Install with all development tools
pip install -r requirements-dev.txt

# Or use setuptools optional dependencies
pip install -e ".[dev]"
```

---

## Platform-Specific Setup

### Windows 10/11

#### Step 1: Install Python

- Download from [python.org](https://www.python.org/downloads/)
- **Important**: Check "Add Python to PATH" during installation
- Verify: `python --version` in Command Prompt or PowerShell

#### Step 2: Install Dependencies

```powershell
cd C:\path\to\blog_visual_engine
pip install -r requirements.txt
```

#### Step 3: Verify Text-to-Speech

```powershell
python -c "import pyttsx3; tts = pyttsx3.init(); print('TTS OK')"
```

#### Step 4: Check Available Voices

```powershell
python -c "
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(f'Found {len(voices)} voices')
for v in voices:
    print(f'  - {v.name}')
"
```

**Troubleshooting Windows TTS:**

- If no voices appear: Ensure Windows Speech Platform is installed
  - Settings → Time & Language → Speech
  - Verify a voice is set as default
- If audio fails: Check audio output device is enabled
- If pyttsx3 hangs: May be accessing audio drivers, wait 10-30 seconds

---

### macOS 10.13+

#### Step 1: Install Python

Using Homebrew (recommended):

```bash
brew install python3
```

Or download from [python.org](https://www.python.org/downloads/)

#### Step 2: Install Dependencies

```bash
cd /path/to/blog_visual_engine
pip3 install -r requirements.txt
```

#### Step 3: Verify Text-to-Speech

```bash
python3 -c "import pyttsx3; tts = pyttsx3.init(); print('TTS OK')"
```

**Note**: macOS uses NSSpeechSynthesizer (built-in). Voices are system-managed.

---

### Linux (Ubuntu/Debian 20.04+)

#### Step 1: Install Python and System Dependencies

```bash
# Update package manager
sudo apt-get update

# Install Python 3.8+
sudo apt-get install python3 python3-pip python3-dev

# Install TTS backend (choose one)
sudo apt-get install espeak-ng
# OR
sudo apt-get install festival

# Install audio system (if not present)
sudo apt-get install alsa-utils pulseaudio
```

#### Step 2: Configure pyttsx3 Driver

```bash
# Set environment variable for espeak driver
export PYTTSX3_DRIVER=espeak
# Or for festival:
export PYTTSX3_DRIVER=festival

# Add to ~/.bashrc to persist:
echo 'export PYTTSX3_DRIVER=espeak' >> ~/.bashrc
source ~/.bashrc
```

#### Step 3: Install Python Dependencies

```bash
cd /path/to/blog_visual_engine
pip3 install -r requirements.txt
```

#### Step 4: Verify Text-to-Speech

```bash
python3 -c "import pyttsx3; tts = pyttsx3.init(); print('TTS OK')"
```

**Troubleshooting Linux TTS:**

- If no sound: Check ALSA/PulseAudio: `pactl info` or `alsamixer`
- If espeak not found: `sudo apt-get install espeak-ng`
- If pyttsx3 driver fails: `PYTTSX3_DRIVER=espeak python3 script.py`

---

## Dependency Details

### Core Dependencies

| Package   | Version | Purpose            | Notes                             |
| --------- | ------- | ------------------ | --------------------------------- |
| `pyttsx3` | ≥2.90   | Offline TTS        | No API key needed, cross-platform |
| `pillow`  | ≥9.0.0  | Image processing   | For slides and chart generation   |
| `pydub`   | ≥0.25.1 | Audio manipulation | WAV/MP3 file handling             |

### Development Dependencies

| Package      | Version | Purpose                  |
| ------------ | ------- | ------------------------ |
| `pytest`     | ≥7.0.0  | Unit testing             |
| `pytest-cov` | ≥4.0.0  | Test coverage reports    |
| `black`      | ≥22.0.0 | Code formatting          |
| `flake8`     | ≥4.0.0  | Code linting             |
| `mypy`       | ≥0.990  | Static type checking     |
| `isort`      | ≥5.10.0 | Import sorting           |
| `sphinx`     | ≥5.0.0  | Documentation generation |
| `pylint`     | ≥2.15.0 | Advanced linting         |
| `coverage`   | ≥6.0    | Coverage analysis        |

### Optional Dependencies

- `matplotlib` (≥3.5.0): Enhanced chart generation
- `scipy` (≥1.8.0): Statistical chart types
- `opencv-python` (≥4.5.0): Video processing
- `ffmpeg-python` (≥0.2.1): FFmpeg wrapper
- `ffmpeg` binary: Install via system package manager

---

## Installation Verification

### Run Test Suite

```bash
cd blog_visual_engine
pytest tests/ -v
```

### Run Specific Tests

```bash
# Test imports
pytest tests/test_imports.py -v

# Test with coverage
pytest tests/ --cov=blog_visual_engine --cov-report=html
```

### Run Examples

```bash
# TTS Demo
python examples/tts_demo.py

# Minimal Post Example
python examples/minimal_post/build.py
```

---

## Troubleshooting Installation

### Issue: "ModuleNotFoundError: No module named 'pyttsx3'"

**Solution:**

```bash
pip install --upgrade pyttsx3
# Or reinstall all dependencies
pip install --force-reinstall -r requirements.txt
```

### Issue: "pyttsx3 hangs or freezes"

**Solution:** This often happens on first run while initializing audio drivers.

- Wait 10-30 seconds
- Check audio output device is available
- Try with specific driver: `PYTTSX3_DRIVER=espeak python script.py`
- Restart terminal/IDE

### Issue: "No voices available" or "No module named '\_winvoice'"

**Solution:**

```bash
# Windows: Ensure speech platform is installed
# Settings → Time & Language → Speech → Manage Voices

# macOS: Check system voices
python3 -c "import pyttsx3; print(pyttsx3.init().getProperty('voices'))"

# Linux: Ensure espeak is installed
sudo apt-get install espeak-ng
export PYTTSX3_DRIVER=espeak
```

### Issue: "Permission denied" on Linux

**Solution:**

```bash
# Use user installation
pip install --user -r requirements.txt

# Or use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: "pip: command not found"

**Solution:**

```bash
# Use python -m pip instead
python -m pip install -r requirements.txt

# Or ensure pip is installed
python -m ensurepip --upgrade
```

---

## Virtual Environment Setup (Recommended)

### Windows

```powershell
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### macOS/Linux

```bash
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Deactivate:**

```bash
deactivate
```

---

## Development Workflow

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/Hysnap/AutoBlogVideoNpodCast.git
cd blog_visual_engine

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\Activate.ps1

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Or use requirements file
pip install -r requirements-dev.txt
```

### Running Code Quality Checks

```bash
# Format code
black blog_visual_engine/ examples/ tests/

# Lint code
flake8 blog_visual_engine/ examples/ tests/

# Type checking
mypy blog_visual_engine/

# Sort imports
isort blog_visual_engine/ examples/ tests/

# Run tests with coverage
pytest tests/ --cov=blog_visual_engine --cov-report=html
```

### Building Documentation

```bash
# Install sphinx (included in requirements-dev.txt)
pip install sphinx sphinx-rtd-theme

# Build HTML docs
cd docs
make html

# View: docs/_build/html/index.html
```

---

## Upgrading Dependencies

### Check for Outdated Packages

```bash
pip list --outdated
```

### Upgrade Specific Package

```bash
pip install --upgrade pyttsx3
```

### Upgrade All Dependencies

```bash
pip install --upgrade -r requirements.txt
```

### Freeze Current Environment

```bash
pip freeze > requirements-locked.txt
```

---

## Docker Installation (Optional)

### Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    espeak-ng \
    && rm -rf /var/lib/apt/lists/*

# Set TTS driver
ENV PYTTSX3_DRIVER=espeak

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application
COPY . .

CMD ["bash"]
```

### Build and Run

```bash
docker build -t blog-visual-engine .
docker run -it blog-visual-engine
```

---

## Getting Help

### Check Installation

```bash
# Verify all imports work
python -c "
from blog_visual_engine.audio.tts import TextToSpeech
from blog_visual_engine.config.theme import Theme
from blog_visual_engine.visuals.charts import ChartGenerator
from blog_visual_engine.slides.impress import Presentation
print('✅ All imports successful')
"
```

### View Installed Package Info

```bash
pip show blog-visual-engine
pip show pyttsx3
```

### Check Requirements Versions

```bash
pip list | grep -E "(pyttsx3|pillow|pydub|pytest)"
```

---

**Last Updated**: January 22, 2026  
**Maintained By**: AutoBlogVideoNpodCast Team
