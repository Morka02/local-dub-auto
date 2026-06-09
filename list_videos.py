#!/usr/bin/env python3
"""Read rclone lsjson on stdin, print ALL video file names, oldest first,
one per line. Used by the auto-dub workflow to build the processing queue."""
import sys
import json

VIDEO_EXTS = (".mp4", ".mkv", ".mov", ".avi", ".webm", ".m4v", ".flv", ".ts")


def main() -> None:
    try:
        items = json.load(sys.stdin)
    except Exception:
        items = []
    vids = [
        i for i in items
        if not i.get("IsDir", False)
        and i.get("Name", "").lower().endswith(VIDEO_EXTS)
    ]
    vids.sort(key=lambda i: i.get("ModTime", ""))
    for v in vids:
        print(v["Name"])


if __name__ == "__main__":
    main()
