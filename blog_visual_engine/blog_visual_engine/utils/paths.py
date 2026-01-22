"""Path utilities and file management."""

from pathlib import Path
from typing import Optional
import os


class PathManager:
    """Manage project paths and file operations."""


    def __init__(self, project_root: Optional[Path] = None):
        """
        Initialize path manager.

        Args:
            project_root: Root directory for the project
        """
        self.project_root = project_root or Path.cwd()
        self.output_dir = self.project_root / "output"
        self.cache_dir = self.project_root / ".cache"


    def setup_directories(self) -> None:
        """Create necessary project directories."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Create subdirectories
        (self.output_dir / "videos").mkdir(exist_ok=True)
        (self.output_dir / "audio").mkdir(exist_ok=True)
        (self.output_dir / "slides").mkdir(exist_ok=True)


    def get_output_path(self, filename: str, subdir: str = "") -> Path:
        """
        Get path for output file.

        Args:
            filename: Name of output file
            subdir: Optional subdirectory within output

        Returns:
            Full path for output file
        """
        if subdir:
            path = self.output_dir / subdir / filename
            path.parent.mkdir(parents=True, exist_ok=True)
        else:
            path = self.output_dir / filename

        return path


    def get_cache_path(self, key: str) -> Path:
        """
        Get path for cached data.

        Args:
            key: Cache key/identifier
            
        Returns:
            Path to cache file
        """
        return self.cache_dir / f"{key}.cache"


    def clean_output(self) -> None:
        """Remove all files in output directory."""
        if self.output_dir.exists():
            for item in self.output_dir.iterdir():
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    self._rmtree(item)


    def clean_cache(self) -> None:
        """Remove all cached files."""
        if self.cache_dir.exists():
            for item in self.cache_dir.iterdir():
                if item.is_file():
                    item.unlink()


    @staticmethod
    def _rmtree(path: Path) -> None:
        """Recursively remove directory."""
        for child in path.iterdir():
            if child.is_file():
                child.unlink()
            else:
                PathManager._rmtree(child)
        path.rmdir()


    @staticmethod
    def ensure_exists(path: Path) -> Path:
        """
        Ensure a path exists, creating it if necessary.

        Args:
            path: Path to ensure exists

        Returns:
            The path
        """
        path.mkdir(parents=True, exist_ok=True)
        return path
