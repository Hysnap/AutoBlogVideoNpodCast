"""Text-to-speech audio generation using offline pyttsx3 library."""

import pyttsx3
from pathlib import Path
from typing import Optional, List
import os


class TextToSpeech:
    """Handle offline text-to-speech conversion using pyttsx3."""

    def __init__(self, voice_id: Optional[str] = None, speed: int = 150, volume: float = 1.0):
        """
        Initialize TTS engine using pyttsx3 (offline).

        Args:
            voice_id: Voice identifier (None for default system voice)
            speed: Speech rate in words per minute (default: 150)
            volume: Volume level from 0.0 to 1.0 (default: 1.0)
        """
        self.engine = pyttsx3.init()
        self.speed = speed
        self.volume = volume
        self.voice_id = voice_id
        
        # Configure engine
        self.engine.setProperty('rate', speed)
        self.engine.setProperty('volume', volume)
        
        # Set voice if specified
        if voice_id:
            self.engine.setProperty('voice', voice_id)
        else:
            # Get default voice
            voices = self.engine.getProperty('voices')
            if voices:
                self.voice_id = voices[0].id
    
    def list_available_voices(self) -> List[dict]:
        """
        Get list of all available system voices.
        
        Returns:
            List of dictionaries containing voice information
        """
        voices = self.engine.getProperty('voices')
        return [
            {
                'id': voice.id,
                'name': voice.name,
                'languages': voice.languages,
                'gender': voice.gender,
                'age': voice.age
            }
            for voice in voices
        ]

    def synthesize(self, text: str, output_path: Path) -> Path:
        """
        Convert text to speech audio file.

        Args:
            text: Text to synthesize
            output_path: Path for output audio file (must be .wav)
            
        Returns:
            Path to generated audio file
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Ensure output is WAV format
        if output_path.suffix.lower() != '.wav':
            output_path = output_path.with_suffix('.wav')
        
        # Save to file
        self.engine.save_to_file(text, str(output_path))
        self.engine.runAndWait()
        
        return output_path


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

        # Queue all segments for synthesis at once to avoid engine hang
        for i, text in enumerate(text_segments):
            output_path = output_dir / f"segment_{i:03d}.wav"
            
            # Ensure output is WAV format
            if output_path.suffix.lower() != '.wav':
                output_path = output_path.with_suffix('.wav')
            
            self.engine.save_to_file(text, str(output_path))
            audio_files.append(output_path)
        
        # Process all queued segments at once
        self.engine.runAndWait()
        
        # Reinitialize engine to prevent hang on Windows
        self._reinitialize_engine()

        return audio_files

    def set_voice(self, voice_id: str) -> None:
        """
        Change the TTS voice.
        
        Args:
            voice_id: Voice identifier from list_available_voices()
        """
        self.voice_id = voice_id
        self.engine.setProperty('voice', voice_id)

    def set_speed(self, speed: int) -> None:
        """
        Set speech speed.

        Args:
            speed: Words per minute (typical range: 100-200)
        """
        if speed <= 0:
            raise ValueError("Speed must be positive")
        self.speed = speed
        self.engine.setProperty('rate', speed)
    
    def set_volume(self, volume: float) -> None:
        """
        Set speech volume.
        
        Args:
            volume: Volume level from 0.0 to 1.0
        """
        if not 0.0 <= volume <= 1.0:
            raise ValueError("Volume must be between 0.0 and 1.0")
        self.volume = volume
        self.engine.setProperty('volume', volume)

    def speak(self, text: str) -> None:
        """
        Speak text immediately without saving to file.
        
        Args:
            text: Text to speak
        """
        self.engine.say(text)
        self.engine.runAndWait()

    def estimate_duration(self, text: str) -> float:
        """
        Estimate audio duration for text.

        Args:
            text: Input text
            
        Returns:
            Estimated duration in seconds
        """
        words = len(text.split())
        # Convert words per minute to seconds
        duration = (words / self.speed) * 60
        return duration
    
    def stop(self) -> None:
        """Stop the current speech."""
        self.engine.stop()
    
    def _reinitialize_engine(self) -> None:
        """Reinitialize the TTS engine to prevent hang issues on Windows."""
        try:
            self.engine.stop()
        except:
            pass
        
        # Reinitialize with same settings
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', self.speed)
        self.engine.setProperty('volume', self.volume)
        if self.voice_id:
            self.engine.setProperty('voice', self.voice_id)
    
    def __del__(self):
        """Cleanup TTS engine."""
        try:
            self.engine.stop()
        except:
            pass
