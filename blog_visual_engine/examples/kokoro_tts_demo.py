"""Demo script for Kokoro TTS text-to-speech functionality."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from blog_visual_engine.audio.kokoro_tts import KokoroTTS


def main():
    """Demonstrate Kokoro TTS capabilities."""
    
    print("=" * 60)
    print("Kokoro TTS Demo - High Quality Neural Text-to-Speech")
    print("=" * 60)
    print()
    
    # Initialize TTS engine
    print("🎙️  Initializing Kokoro TTS engine...")
    try:
        tts = KokoroTTS(voice="af_sarah", speed=1.0)
        print("✅ Kokoro TTS engine initialized")
    except RuntimeError as e:
        print(f"❌ Error: {e}")
        return
    print()
    
    # List available voices
    print("📋 Available Kokoro voices:")
    print("-" * 60)
    voices = tts.list_available_voices()
    for i, voice in enumerate(voices, 1):
        print(f"{i:2d}. {voice['name']:<30} ({voice['gender']}, {voice['language']})")
        print(f"     ID: {voice['id']}")
        print()
    
    # Sample text
    sample_text = """
    Hello! This is a demonstration of Kokoro TTS, a high-quality neural text-to-speech system.
    Kokoro offers natural-sounding voices with excellent prosody and intonation.
    It works entirely offline after initial setup, giving you full control over your audio generation.
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
    output_path = output_dir / "kokoro_demo_speech.wav"
    
    print(f"🔊 Generating audio file: {output_path.name}")
    try:
        result_path = tts.synthesize(sample_text, output_path)
        print(f"✅ Audio file saved: {result_path}")
        file_size_kb = result_path.stat().st_size / 1024
        print(f"📁 File size: {file_size_kb:.1f} KB")
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    print()
    
    # Demonstrate batch processing
    print("=" * 60)
    print("📦 Batch processing demo:")
    print("-" * 60)
    
    text_segments = [
        "This is the first segment of our demonstration.",
        "Here comes the second segment with different content.",
        "And finally, this is the third and last segment.",
    ]
    
    batch_output = output_dir / "kokoro_batch"
    print(f"Generating {len(text_segments)} audio segments...")
    try:
        audio_files = tts.synthesize_batch(text_segments, batch_output)
        
        for i, file in enumerate(audio_files, 1):
            file_size = file.stat().st_size / 1024
            print(f"  {i}. {file.name} ({file_size:.1f} KB)")
        print("✅ Batch processing complete")
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    print()
    
    # Voice comparison demo
    print("=" * 60)
    print("🎭 Voice comparison demo:")
    print("-" * 60)
    
    comparison_text = "Hello, this is a voice comparison test."
    comparison_voices = ["af_sarah", "am_adam", "bf_emma", "bm_george"]
    
    print("Generating samples with different voices...")
    voice_dir = output_dir / "voice_comparison"
    
    for voice_id in comparison_voices:
        try:
            tts.set_voice(voice_id)
            voice_path = voice_dir / f"{voice_id}.wav"
            tts.synthesize(comparison_text, voice_path)
            print(f"  ✓ {voice_id}")
        except Exception as e:
            print(f"  ✗ {voice_id}: {e}")
    
    print()
    print("=" * 60)
    print("✨ Demo complete!")
    print(f"📁 Output directory: {output_dir}")
    print("=" * 60)
    print()
    print("💡 Tip: You can play the generated WAV files with any audio player")


if __name__ == "__main__":
    main()
