"""Test that all modules can be imported successfully."""

import pytest


def test_import_main_package():
    """Test importing main package."""
    import blog_visual_engine
    assert blog_visual_engine.__version__


def test_import_config_modules():
    """Test importing config modules."""
    from blog_visual_engine.config import theme, defaults
    from blog_visual_engine.config.theme import Theme
    from blog_visual_engine.config.defaults import DEFAULT_CONFIG, get_config

    assert Theme is not None
    assert DEFAULT_CONFIG is not None
    assert callable(get_config)


def test_import_visual_modules():
    """Test importing visual modules."""
    from blog_visual_engine.visuals import charts, layouts
    from blog_visual_engine.visuals.charts import ChartGenerator
    from blog_visual_engine.visuals.layouts import Layout, LayoutType

    assert ChartGenerator is not None
    assert Layout is not None
    assert LayoutType is not None


def test_import_slides_module():
    """Test importing slides module."""
    from blog_visual_engine.slides import impress
    from blog_visual_engine.slides.impress import Slide, Presentation

    assert Slide is not None
    assert Presentation is not None


def test_import_audio_module():
    """Test importing audio module."""
    from blog_visual_engine.audio import tts
    from blog_visual_engine.audio.tts import TextToSpeech

    assert TextToSpeech is not None


def test_import_utils_module():
    """Test importing utils module."""
    from blog_visual_engine.utils import paths
    from blog_visual_engine.utils.paths import PathManager

    assert PathManager is not None


def test_theme_creation():
    """Test creating a Theme instance."""
    from blog_visual_engine.config.theme import Theme

    theme = Theme()
    assert theme.primary_color == (41, 128, 185)
    assert theme.slide_width == 1920
    assert theme.slide_height == 1080


def test_get_config():
    """Test configuration getter."""
    from blog_visual_engine.config.defaults import get_config

    fps = get_config("video.fps")
    assert fps == 30

    invalid = get_config("invalid.key", default="default_value")
    assert invalid == "default_value"


def test_layout_creation():
    """Test creating a Layout instance."""
    from blog_visual_engine.visuals.layouts import Layout

    layout = Layout(1920, 1080)
    assert layout.width == 1920
    assert layout.height == 1080

    x, y = layout.center_element(100, 100)
    assert x == (1920 - 100) // 2
    assert y == (1080 - 100) // 2


def test_presentation_creation():
    """Test creating a Presentation."""
    from blog_visual_engine.slides.impress import Presentation, Slide

    pres = Presentation("Test Presentation")
    assert pres.title == "Test Presentation"
    assert len(pres.slides) == 0

    slide = Slide(title="Test Slide", content="Content")
    pres.add_slide(slide)
    assert len(pres.slides) == 1


def test_tts_initialization():
    """Test TextToSpeech initialization."""
    from blog_visual_engine.audio.tts import TextToSpeech

    tts = TextToSpeech(voice="en-US-Neural", speed=1.0)
    assert tts.voice == "en-US-Neural"
    assert tts.speed == 1.0
    assert tts.sample_rate == 44100


def test_path_manager():
    """Test PathManager initialization."""
    from blog_visual_engine.utils.paths import PathManager
    from pathlib import Path

    pm = PathManager()
    assert pm.project_root == Path.cwd()
    assert pm.output_dir == Path.cwd() / "output"
    assert pm.cache_dir == Path.cwd() / ".cache"
