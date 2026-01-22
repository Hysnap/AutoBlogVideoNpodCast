"""Demo script for offline text-to-speech functionality."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from blog_visual_engine.audio.tts import TextToSpeech


def main():
    """Demonstrate offline TTS capabilities."""
    
    print("=" * 60)
    print("Offline Text-to-Speech Demo using pyttsx3")
    print("=" * 60)
    print()
    
    # Initialize TTS engine
    print("🎙️  Initializing offline TTS engine...")
    tts = TextToSpeech(speed=150, volume=0.9)
    print("✅ TTS engine initialized")
    print()
    
    # List available voices
    print("📋 Available system voices:")
    print("-" * 60)
    voices = tts.list_available_voices()
    for i, voice in enumerate(voices, 1):
        print(f"{i}. {voice['name']}")
        print(f"   ID: {voice['id']}")
        print(f"   Languages: {voice.get('languages', 'N/A')}")
        print()
    
    # Sample text
    sample_text = """
    Hello! This is a demonstration of offline text-to-speech conversion.
    This tool uses pyttsx3, which works entirely offline without requiring
    any internet connection or API keys. It uses your system's built-in
    speech synthesis capabilities.
    """
    
    print("=" * 60)
    print("📝 Sample text to convert:")
    print("-" * 60)
    print(sample_text.strip())
    print()
    
    # Estimate duration
    duration = tts.estimate_duration(sample_text)
    print(f"⏱️  Estimated duration: {duration:.1f} seconds")
    print()
    
    # Generate audio file
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "demo_speech.wav"
    
    print(f"🔊 Generating audio file: {output_path.name}")
    result_path = tts.synthesize(sample_text, output_path)
    print(f"✅ Audio file saved: {result_path}")
    print()
    
    # Demonstrate batch processing
    print("=" * 60)
    print("📦 Batch processing demo:")
    print("-" * 60)
    
    text_segments = [
        "This is segment one.",
        "This is segment two.",
        "This is segment three.",
    ]
    
    batch_output = output_dir / "batch"
    print(f"Generating {len(text_segments)} audio segments...")
    audio_files = tts.synthesize_batch(text_segments, batch_output)
    
    for i, file in enumerate(audio_files, 1):
        print(f"  {i}. {file.name}")
    print("✅ Batch processing complete")
    print()
    
    # Demonstrate live speech (optional)
    print("=" * 60)
    print("🔈 Live speech demo:")
    user_input = input("Enter text to speak aloud (or press Enter to skip): ").strip()
    
    if user_input:
        print("🗣️  Speaking...")
        tts.speak(user_input)
        print("✅ Done speaking")
    else:
        print("⏭️  Skipped")
    
    print()
    print("=" * 60)
    print("✨ Demo complete!")
    print(f"📁 Output directory: {output_dir}")
    print("=" * 60)


if __name__ == "__main__":
    main()
