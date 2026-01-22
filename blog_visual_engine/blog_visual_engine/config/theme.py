"""Theme configuration for visual elements."""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Theme:
    """Visual theme configuration."""
    
    # Colors (RGB tuples)
    primary_color: Tuple[int, int, int] = (41, 128, 185)
    secondary_color: Tuple[int, int, int] = (52, 73, 94)
    background_color: Tuple[int, int, int] = (255, 255, 255)
    text_color: Tuple[int, int, int] = (44, 62, 80)
    accent_color: Tuple[int, int, int] = (231, 76, 60)
    
    # Typography
    font_family: str = "Arial"
    heading_size: int = 48
    body_size: int = 24
    
    # Layout
    slide_width: int = 1920
    slide_height: int = 1080
    padding: int = 100
    
    def __post_init__(self):
        """Validate theme configuration."""
        if self.slide_width <= 0 or self.slide_height <= 0:
            raise ValueError("Slide dimensions must be positive")
