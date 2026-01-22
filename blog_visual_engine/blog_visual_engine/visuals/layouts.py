"""Layout management for visual elements."""

from typing import Tuple, Optional
from enum import Enum


class LayoutType(Enum):
    """Available layout types."""
    TITLE = "title"
    CONTENT = "content"
    TWO_COLUMN = "two_column"
    IMAGE_TEXT = "image_text"
    FULL_IMAGE = "full_image"


class Layout:
    """Manage slide layouts and positioning."""


    def __init__(self, width: int = 1920, height: int = 1080):
        """
        Initialize layout manager.

        Args:
            width: Slide width in pixels
            height: Slide height in pixels
        """
        self.width = width
        self.height = height
        self.padding = 100


    def get_title_bounds(self) -> Tuple[int, int, int, int]:
        """
        Get bounding box for title area.

        Returns:
            Tuple of (x, y, width, height)
        """
        return (
            self.padding,
            self.padding,
            self.width - 2 * self.padding,
            200
        )


    def get_content_bounds(self) -> Tuple[int, int, int, int]:
        """
        Get bounding box for main content area.

        Returns:
            Tuple of (x, y, width, height)
        """
        title_height = 200
        return (
            self.padding,
            self.padding + title_height + 50,
            self.width - 2 * self.padding,
            self.height - title_height - 3 * self.padding
        )


    def get_two_column_bounds(self) -> Tuple[Tuple[int, int, int, int], Tuple[int, int, int, int]]:
        """
        Get bounding boxes for two-column layout.

        Returns:
            Tuple of two (x, y, width, height) tuples for left and right columns
        """
        content_x, content_y, content_width, content_height = self.get_content_bounds()
        column_width = (content_width - 50) // 2

        left_column = (content_x, content_y, column_width, content_height)
        right_column = (content_x + column_width + 50, content_y, column_width, content_height)
        
        return left_column, right_column


    def center_element(self, element_width: int, element_height: int) -> Tuple[int, int]:
        """
        Calculate position to center an element.

        Args:
            element_width: Width of element to center
            element_height: Height of element to center

        Returns:
            Tuple of (x, y) coordinates
        """
        x = (self.width - element_width) // 2
        y = (self.height - element_height) // 2
        return x, y
