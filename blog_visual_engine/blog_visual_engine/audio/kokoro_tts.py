"""Text-to-speech audio generation using Kokoro TTS."""

from pathlib import Path
from typing import Optional, List
import numpy as np
from scipy.io import wavfile
import os


class KokoroTTS:
    """Handle text-to-speech conversion using Kokoro TTS."""

    def __init__(self, voice: str = "af_heart", speed: float = 1.0):
        """
        Initialize Kokoro TTS engine.

        Args:
            voice: Voice model name (af_heart, am_adam, bf_emma, bm_michael, etc.)
            speed: Speech speed multiplier (default: 1.0, range: 0.5-2.0)
        """
        self.voice = voice
        self.speed = speed
        self.kokoro = None
        self.g2p = None
        
        # Check if kokoro is installed
        self._check_installation()
        
        # Initialize the Kokoro engine
        self._initialize_engine()
    
    def _check_installation(self) -> None:
        """Check if Kokoro TTS and dependencies are installed."""
        try:
            import kokoro_onnx
            import soundfile
            from misaki import en, espeak
        except ImportError as e:
            raise RuntimeError(
                f"Missing dependencies: {e}\n"
                "Please install:\n"
                "pip install kokoro-onnx soundfile 'misaki[en]'\n"
            )
    
    def _initialize_engine(self) -> None:
        """Initialize the Kokoro engine with G2P and models."""
        try:
            from kokoro_onnx import Kokoro
            from misaki import en, espeak
            
            # Get model paths from cache or download
            model_dir = self._get_model_dir()
            model_path = model_dir / "kokoro-v1.0.onnx"
            voices_path = model_dir / "voices-v1.0.bin"
            
            # Download models if needed
            if not model_path.exists() or not voices_path.exists():
                print(f"📥 Downloading Kokoro models to {model_dir}...")
                self._download_models(model_dir)
            
            # Initialize G2P (grapheme-to-phoneme)
            fallback = espeak.EspeakFallback(british=False)
            self.g2p = en.G2P(trf=False, british=False, fallback=fallback)
            
            # Initialize Kokoro
            self.kokoro = Kokoro(str(model_path), str(voices_path))
            
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Kokoro engine: {str(e)}")
    
    def _get_model_dir(self) -> Path:
        """Get or create model cache directory."""
        cache_home = os.getenv("XDG_CACHE_HOME") or Path.home() / ".cache"
        model_dir = Path(cache_home) / "kokoro-onnx"
        model_dir.mkdir(parents=True, exist_ok=True)
        return model_dir
    
    def _download_models(self, model_dir: Path) -> None:
        """Download Kokoro models from GitHub releases."""
        import urllib.request
        
        base_url = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
        files = {
            "kokoro-v1.0.onnx": "kokoro-v1.0.onnx",
            "voices-v1.0.bin": "voices-v1.0.bin"
        }
        
        for filename, url_name in files.items():
            file_path = model_dir / filename
            if not file_path.exists():
                url = base_url + url_name
                print(f"   Downloading {filename}...")
                urllib.request.urlretrieve(url, file_path)
                print(f"   ✓ Downloaded {filename}")
    
    def list_available_voices(self) -> List[dict]:
        """
        Get list of all available Kokoro voices.
        
        Returns:
            List of dictionaries containing voice information
        """
        voices = [
            {"id": "af_heart", "name": "Heart (American Female)", "gender": "female", "language": "en-US"},
            {"id": "af_bella", "name": "Bella (American Female)", "gender": "female", "language": "en-US"},
            {"id": "af_nicole", "name": "Nicole (American Female)", "gender": "female", "language": "en-US"},
            {"id": "af_sarah", "name": "Sarah (American Female)", "gender": "female", "language": "en-US"},
            {"id": "af_sky", "name": "Sky (American Female)", "gender": "female", "language": "en-US"},
            {"id": "am_adam", "name": "Adam (American Male)", "gender": "male", "language": "en-US"},
            {"id": "am_michael", "name": "Michael (American Male)", "gender": "male", "language": "en-US"},
            {"id": "bf_emma", "name": "Emma (British Female)", "gender": "female", "language": "en-GB"},
            {"id": "bf_isabella", "name": "Isabella (British Female)", "gender": "female", "language": "en-GB"},
            {"id": "bm_george", "name": "George (British Male)", "gender": "male", "language": "en-GB"},
            {"id": "bm_lewis", "name": "Lewis (British Male)", "gender": "male", "language": "en-GB"},
        ]
        return voices

    def synthesize(self, text: str, output_path: Path) -> Path:
        """
        Convert text to speech audio file using Kokoro TTS.

        Args:
            text: Text to synthesize
            output_path: Path for output audio file (will be converted to WAV)
            
        Returns:
            Path to generated audio file
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Ensure output is WAV format
        if output_path.suffix.lower() != '.wav':
            output_path = output_path.with_suffix('.wav')
        
        try:
            import soundfile as sf
            
            # Convert text to phonemes
            phonemes, _ = self.g2p(text)
            
            # Generate audio using Kokoro
            samples, sample_rate = self.kokoro.create(
                phonemes, 
                self.voice, 
                speed=self.speed,
                is_phonemes=True
            )
            
            # Save as WAV file using soundfile
            sf.write(str(output_path), samples, sample_rate)
            
            if not output_path.exists():
                raise RuntimeError(f"Output file not created: {output_path}")
            
            return output_path
            
        except Exception as e:
            raise RuntimeError(f"Error during synthesis: {str(e)}")

    def synthesize_batch(self, text_segments: List[str], output_dir: Path) -> List[Path]:
        """
        Convert multiple text segments to audio files.

        Args:
            text_segments: List of text strings to synthesize
            output_dir: Directory for output audio files

        Returns:
            List of paths to generated audio files
        """
        output_dir.mkdir(parents=True, exist_ok=True)
        audio_files = []

        for i, text in enumerate(text_segments):
            output_path = output_dir / f"segment_{i:03d}.wav"
            try:
                result_path = self.synthesize(text, output_path)
                audio_files.append(result_path)
            except Exception as e:
                print(f"Warning: Failed to synthesize segment {i}: {e}")
                continue

        return audio_files

    def set_voice(self, voice: str) -> None:
        """
        Change the TTS voice.
        
        Args:
            voice: Voice identifier from list_available_voices()
        """
        valid_voices = [v["id"] for v in self.list_available_voices()]
        if voice not in valid_voices:
            raise ValueError(f"Invalid voice. Choose from: {', '.join(valid_voices)}")
        self.voice = voice

    def set_speed(self, speed: float) -> None:
        """
        Set speech speed.

        Args:
            speed: Speed multiplier (0.5 = half speed, 2.0 = double speed)
        """
        if not 0.5 <= speed <= 2.0:
            raise ValueError("Speed must be between 0.5 and 2.0")
        self.speed = speed
    
    def estimate_duration(self, text: str) -> float:
        """
        Estimate audio duration for text.

        Args:
            text: Input text
            
        Returns:
            Estimated duration in seconds
        """
        # Kokoro speaks at approximately 150-180 words per minute at speed 1.0
        words = len(text.split())
        base_wpm = 165
        adjusted_wpm = base_wpm * self.speed
        duration = (words / adjusted_wpm) * 60
        return duration
