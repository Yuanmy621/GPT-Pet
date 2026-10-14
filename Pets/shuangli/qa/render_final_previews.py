"""Export animation previews from an existing v1/v2 pet atlas; never draw art."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PET_DIR = Path(__file__).resolve().parents[1]
REPO_DIR = PET_DIR.parents[1]
CELL_WIDTH, CELL_HEIGHT = 192, 208
ROW_DURATIONS = {
    "idle": [280, 110, 110, 140, 140, 320],
    "running-right": [120] * 7 + [220],
    "running-left": [120] * 7 + [220],
    "waving": [140] * 3 + [280],
    "jumping": [140] * 4 + [280],
    "failed": [140] * 7 + [240],
    "waiting": [150] * 5 + [260],
    "running": [120] * 5 + [220],
    "review": [150] * 5 + [280],
}


def save_gif(frames: list[Image.Image], durations: list[int], path: Path) -> None:
    frames[0].save(
        path, save_all=True, append_images=frames[1:], duration=durations,
        loop=0, disposal=2, optimize=False,
    )


def labeled_frame(frame: Image.Image, title: str) -> Image.Image:
    canvas = Image.new("RGB", (240, 256), "#ececf5")
    canvas.paste(frame, (24, 36), frame)
    ImageDraw.Draw(canvas).text(
        (12, 10), title, font=ImageFont.load_default(size=16), fill="#38354e",
    )
    return canvas


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("atlas", nargs="?", type=Path,
                        default=PET_DIR / "final/spritesheet-extended.png")
    parser.add_argument("--output-dir", type=Path, default=PET_DIR / "previews")
    parser.add_argument("--skip-mp4", action="store_true")
    args = parser.parse_args()
    atlas_path = args.atlas.expanduser().resolve()
    output = args.output_dir.expanduser().resolve()
    with Image.open(atlas_path) as source:
        if source.size not in {(1536, 1872), (1536, 2288)}:
            parser.error("atlas must be 1536x1872 (v1) or 1536x2288 (v2)")
        atlas = source.convert("RGBA")
    output.mkdir(parents=True, exist_ok=True)
    frames_root = output / "final-frames"

    def cell(row: int, column: int) -> Image.Image:
        left, top = column * CELL_WIDTH, row * CELL_HEIGHT
        return atlas.crop((left, top, left + CELL_WIDTH, top + CELL_HEIGHT))

    all_frames, all_durations, stills = [], [], []
    for row, (state, durations) in enumerate(ROW_DURATIONS.items()):
        state_dir = frames_root / state
        state_dir.mkdir(parents=True, exist_ok=True)
        frames = [cell(row, column) for column in range(len(durations))]
        for column, frame in enumerate(frames):
            frame.save(state_dir / f"{column:02d}.png")
            all_frames.append(labeled_frame(frame, state))
        all_durations.extend(durations)
        save_gif(frames, durations, output / f"{state}.gif")
        if state in {"idle", "waving", "jumping", "failed"}:
            column = 0 if state == "idle" else 2
            stills.append(labeled_frame(frames[column], f"{state} / frame {column + 1}"))

    save_gif(all_frames, all_durations, output / "all-states.gif")
    transition = ([cell(0, i) for i in range(6)] + [cell(4, i) for i in range(5)]
                  + [cell(0, i) for i in range(6)])
    save_gif(transition, ROW_DURATIONS["idle"] + ROW_DURATIONS["jumping"]
             + ROW_DURATIONS["idle"], output / "idle-jump-idle.gif")
    if atlas.height == 2288:
        save_gif([cell(9 + i // 8, i % 8) for i in range(16)],
                 [180] * 16, output / "look-loop.gif")

    proof = Image.new("RGB", (960, 256), "#ececf5")
    for index, frame in enumerate(stills):
        proof.paste(frame, (index * 240, 0))
    proof.save(output / "motion-stills.png")

    if not args.skip_mp4:
        try:
            import imageio_ffmpeg
        except ImportError:
            parser.error("install requirements.txt or use --skip-mp4")
        try:
            subprocess.run(
                [imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-i", str(output / "all-states.gif"),
                 "-an", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                 str(output / "all-states.mp4")], check=True, capture_output=True,
            )
        except subprocess.CalledProcessError as error:
            parser.error(error.stderr.decode(errors="replace"))

    try:
        source_label = atlas_path.relative_to(REPO_DIR).as_posix()
    except ValueError:
        source_label = atlas_path.name
    (output / "preview-source.json").write_text(json.dumps({
        "source_atlas": source_label, "all_states": list(ROW_DURATIONS),
        "source_is_final_encoded_sheet": True,
        "sprite_version": 2 if atlas.height == 2288 else 1,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "output_dir": str(output)}))


if __name__ == "__main__":
    main()
