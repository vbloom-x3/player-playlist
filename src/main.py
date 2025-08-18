#!/usr/bin/env python3
import subprocess
import sys
import os
import re

def normalize_path(path):
    # Convert Windows backslashes to Unix forward slashes
    path = path.replace("\\", "/")

    # If it's an absolute Windows path like C:/Music/track.mp3, keep it usable on WSL/Linux
    # Strip drive letters (C:/) if present
    if re.match(r"^[A-Za-z]:/", path):
        path = "/" + path[0].lower() + path[2:]

    return os.path.normpath(path)

def parse_m3u8(file_path):
    """Parse .m3u8 playlist and return a list of normalized track paths."""
    tracks = []
    base_dir = os.path.dirname(file_path)

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Normalize path and handle relative paths
            normalized = normalize_path(line)
            if not os.path.isabs(normalized):
                normalized = os.path.join(base_dir, normalized)
            tracks.append(os.path.abspath(normalized))

    return tracks

def main():
    if len(sys.argv) < 2:
        print("Usage: player-playlist.py <playlist.m3u8>")
        sys.exit(1)

    playlist_path = sys.argv[1]
    if not os.path.isfile(playlist_path):
        print(f"Error: File '{playlist_path}' not found")
        sys.exit(1)

    tracks = parse_m3u8(playlist_path)
    if not tracks:
        print("No valid tracks found in the playlist!")
        sys.exit(1)

    for track in tracks:
        print(f"▶ Now playing: {track}")
        try:
            # Call your existing player script for each track
            subprocess.run(["python3", "/home/{}/.local/bin/player.py".format(os.getenv("USER")), track])
            subprocess.run(["python3", /home/{}/.local/bin/img.py", "cover.jpg"])
        except KeyboardInterrupt:
            print("\nStopped by user.")
            sys.exit(0)

if __name__ == "__main__":
    main()
