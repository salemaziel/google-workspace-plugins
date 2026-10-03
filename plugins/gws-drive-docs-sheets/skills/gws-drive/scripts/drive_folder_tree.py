#!/usr/bin/env python3
"""
drive_folder_tree.py - Construct an ASCII directory tree from Google Drive JSON listing.

Usage:
  gws drive files list --params '{"q": "trashed = false", "fields": "files(id, name, mimeType, parents)"}' | ./scripts/drive_folder_tree.py
"""

import sys
import json
from collections import defaultdict

def main():
    try:
        raw = sys.stdin.read().strip()
        if not raw:
            print("No JSON input provided on stdin.", file=sys.stderr)
            sys.exit(1)
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}", file=sys.stderr)
        sys.exit(1)

    files = data if isinstance(data, list) else data.get("files", [])
    if not files:
        print("No files found.")
        return

    by_id = {f["id"]: f for f in files}
    children_map = defaultdict(list)
    root_nodes = []

    for f in files:
        parents = f.get("parents", [])
        if not parents:
            root_nodes.append(f["id"])
        else:
            for p in parents:
                if p not in by_id:
                    root_nodes.append(f["id"])
                else:
                    children_map[p].append(f["id"])

    # Dedup root nodes
    root_nodes = list(dict.fromkeys(root_nodes))

    def print_node(node_id, prefix=""):
        f = by_id.get(node_id)
        if not f:
            return
        is_folder = f.get("mimeType") == "application/vnd.google-apps.folder"
        name = f.get("name", "Untitled")
        icon = "📁 " if is_folder else "📄 "
        print(f"{prefix}{icon}{name} ({f.get('id', '')[:8]}...)")
        children = children_map.get(node_id, [])
        for i, child_id in enumerate(children):
            is_last = (i == len(children) - 1)
            new_prefix = prefix + ("└── " if is_last else "├── ")
            child_prefix = prefix + ("    " if is_last else "│   ")
            print_node(child_id, prefix=child_prefix)

    print("=== Google Drive File Hierarchy ===")
    for r in root_nodes:
        print_node(r)

if __name__ == "__main__":
    main()
