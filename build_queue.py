#!/usr/bin/env python3
"""Build the matrix queue JSON.

Inputs (files in cwd, both optional):
  queue.txt      - one Drive video filename per line
  links_raw.txt  - text dump of link files / manual url; http(s) lines are taken
Prints a JSON array of {"kind": "file"|"url", "ref": ...} objects.
"""
import json
import os

items = []
if os.path.exists("queue.txt"):
    for line in open("queue.txt", encoding="utf-8"):
        line = line.rstrip("\n").strip()
        if line:
            items.append({"kind": "file", "ref": line})
if os.path.exists("links_raw.txt"):
    seen = set()
    for line in open("links_raw.txt", encoding="utf-8", errors="ignore"):
        line = line.strip()
        if line.lower().startswith(("http://", "https://")) and line not in seen:
            seen.add(line)
            items.append({"kind": "url", "ref": line})
print(json.dumps(items))
