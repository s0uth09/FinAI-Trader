#!/usr/bin/env python3
"""Simple runner for FinAI-Trader skeleton.

Prints a summary of the project structure to verify the repo was created successfully.
"""
import os
from pathlib import Path


def summarize(path: Path):
    total_files = 0
    total_dirs = 0
    for root, dirs, files in os.walk(path):
        total_dirs += len(dirs)
        total_files += len(files)
    return total_files, total_dirs


def main():
    root = Path(__file__).resolve().parents[1]
    files, dirs = summarize(root)
    print("FinAI-Trader runner")
    print(f"Root: {root}")
    print(f"Total files: {files}")
    print(f"Total directories: {dirs}")
    print("Sample files:")
    for p in sorted(root.glob('src/**/__init__.py'))[:5]:
        print(" -", p.relative_to(root))


if __name__ == '__main__':
    main()
