#!/usr/bin/env python3
"""Command-line tool to convert blog posts to audio narration."""

import argparse
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from blog_visual_engine.audio.tts import TextToSpeech


def read_markdown_file(file_path: Path) -> str:
    """Read and extract text from markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple markdown processing: remove headers, keep paragraphs
    lines = []
    for line in content.split('\n'):
        line = line.strip()
        # Skip empty lines and code blocks
        if not line or line.startswith('```'):
            continue
        # Remove markdown headers (#)
        if line.startswith('#'):
            line = line.lstrip('#').strip()
        # Remove bold/italic markers
        line = line.replace('**', '').replace('*', '')
        # Remove links [text](url) -> text
        while '[' in line and ']' in line:
            start = line.find('[')
            middle = line.find(']', start)
            end = line.find(')', middle)
            if start != -1 and middle != -1 and end != -1:
                text = line[start+1:middle]
                line = line[:start] + text + line[end+1:]
            else:
                break
        
        if line:
            lines.append(line)
    
    return ' '.join(lines)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Convert blog posts to audio narration (offline)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s post.md -o narration.wav
  %(prog)s post.md -o output.wav --speed 160 --volume 0.8
  %(prog)s post.md --list-voices
        """
    )
    
    parser.add_argument(
        'input',
        type=Path,
        help='Input markdown file (blog post)'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=Path,
        help='Output audio file path (default: <input>_audio.wav)'
    )
    
    parser.add_argument(
        '--speed',
        type=int,
        default=150,
        help='Speech speed in words per minute (default: 150)'
    )
    
    parser.add_argument(
        '--volume',
        type=float,
        default=0.9,
        help='Volume level from 0.0 to 1.0 (default: 0.9)'
    )
    
    parser.add_argument(
        '--voice',
        type=str,
        help='Voice ID to use (see --list-voices)'
    )
    
    parser.add_argument(
        '--list-voices',
        action='store_true',
        help='List all available system voices and exit'
    )
    
    args = parser.parse_args()
    
    # Validate input file
    if not args.input.exists():
        print(f"❌ Error: Input file not found: {args.input}", file=sys.stderr)
        return 1
    
    # Initialize TTS
    print("🎙️  Initializing TTS engine...")
    tts = TextToSpeech(
        voice_id=args.voice,
        speed=args.speed,
        volume=args.volume
    )
    
    # List voices if requested
    if args.list_voices:
        print("\n📋 Available system voices:")
        print("=" * 70)
        voices = tts.list_available_voices()
        for i, voice in enumerate(voices, 1):
            print(f"\n{i}. {voice['name']}")
            print(f"   ID: {voice['id']}")
            if voice['languages']:
                print(f"   Languages: {voice['languages']}")
        return 0
    
    # Read and process input
    print(f"📖 Reading blog post: {args.input.name}")
    text = read_markdown_file(args.input)
    
    word_count = len(text.split())
    print(f"📝 Extracted {word_count} words")
    
    # Estimate duration
    duration = tts.estimate_duration(text)
    print(f"⏱️  Estimated duration: {duration:.1f} seconds ({duration/60:.1f} minutes)")
    
    # Determine output path
    if not args.output:
        args.output = args.input.with_stem(f"{args.input.stem}_audio").with_suffix('.wav')
    
    # Generate audio
    print(f"\n🔊 Generating audio...")
    print(f"   Speed: {args.speed} wpm")
    print(f"   Volume: {args.volume}")
    if args.voice:
        print(f"   Voice: {args.voice}")
    
    try:
        result_path = tts.synthesize(text, args.output)
        print(f"\n✅ Success! Audio saved to: {result_path}")
        print(f"📁 File size: {result_path.stat().st_size / 1024:.1f} KB")
        return 0
    except Exception as e:
        print(f"\n❌ Error generating audio: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
