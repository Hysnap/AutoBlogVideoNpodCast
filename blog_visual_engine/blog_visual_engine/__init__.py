"""Blog Visual Engine - Convert blog posts to videos and presentations."""

__version__ = "0.1.0"

from .config.theme import Theme
from .config.defaults import DEFAULT_CONFIG

__all__ = ["Theme", "DEFAULT_CONFIG", "__version__"]
