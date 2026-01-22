"""Build script for minimal blog post example."""

from pathlib import Path
import sys

# Add parent directory to path to import blog_visual_engine
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from blog_visual_engine.config.theme import Theme
from blog_visual_engine.slides.impress import Presentation, Slide
from blog_visual_engine.audio.tts import TextToSpeech
from blog_visual_engine.utils.paths import PathManager


def main():
    """Build video from blog post."""
    # Setup paths
    current_dir = Path(__file__).parent
    post_path = current_dir / "post.md"
    path_manager = PathManager(current_dir)
    path_manager.setup_directories()

    # Read blog post
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"📝 Read blog post: {post_path}")

    # Create theme
    theme = Theme()
    print(f"🎨 Created theme")

    # Create presentation
    presentation = Presentation(title="My First Blog Video")
    presentation.theme = theme

    # Add slides (simplified example)
    intro_slide = Slide(
        title="My First Blog Video",
        content="Welcome to this example!",
        layout_type="title"
    )
    presentation.add_slide(intro_slide)

    print(f"📊 Created presentation with {len(presentation.slides)} slide(s)")

    # Generate audio (example)
    tts = TextToSpeech()
    audio_text = "Welcome to my first blog video. This is a minimal example."

    audio_path = path_manager.get_output_path("narration.wav", "audio")
    print(f"🎙️  Generating audio narration...")

    # This would generate actual audio in a full implementation
    # tts.synthesize(audio_text, audio_path)

    # Render presentation
    output_video = path_manager.get_output_path("my_first_video.mp4", "videos")
    print(f"🎬 Rendering video to: {output_video}")

    # This would create the actual video in a full implementation
    # presentation.export_video(output_video)

    print("✅ Build complete!")
    print(f"   Output directory: {path_manager.output_dir}")


if __name__ == "__main__":
    main()
