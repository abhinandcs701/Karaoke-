import argparse
import subprocess
import sys
from pathlib import Path

def separate(song_path, out_path="output"):
    song = Path(song_path)
    if not song.exists():
        raise FileNotFoundError(f"Cant find {song}")

    demucs_out = Path(out_path) / "_demucs_raw"

    cmd = [sys.executable, "-m", "demucs", "--two-stems=vocals",
           "-o", str(demucs_out), str(song)]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    parser1 = argparse.ArgumentParser(description="Separate vocals from instrumental")
    parser1.add_argument("song")
    parser1.add_argument("--out", default="output")
    args = parser1.parse_args()

    separate(args.song, args.out)