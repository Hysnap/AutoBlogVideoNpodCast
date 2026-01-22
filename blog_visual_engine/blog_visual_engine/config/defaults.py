"""Default configuration values."""

DEFAULT_CONFIG = {
    "video": {
        "fps": 30,
        "duration_per_slide": 5,
        "transition_duration": 0.5,
        "output_format": "mp4",
        "quality": "high",
    },
    "audio": {
        "tts_engine": "default",
        "voice": "en-US-Neural",
        "speed": 1.0,
        "sample_rate": 44100,
    },
    "processing": {
        "max_workers": 4,
        "cache_enabled": True,
        "verbose": False,
    },
    "output": {
        "directory": "output",
        "naming_pattern": "{title}_{timestamp}",
    },
}


def get_config(key: str, default=None):
    """
    Get a configuration value by key path.
    
    Args:
        key: Dot-separated key path (e.g., "video.fps")
        default: Default value if key not found
        
    Returns:
        Configuration value or default
    """
    keys = key.split(".")
    value = DEFAULT_CONFIG
    
    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            return default
    
    return value
