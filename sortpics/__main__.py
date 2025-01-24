"""
File: __main__.py
Project: google-takeout-organizer
File Created: Friday, 24th January 2025 10:48:32 am
Author: tonell-m
"""

import sys
from pathlib import Path

from . import organize_pictures_by_month

if len(sys.argv) < 2:
    print("Error - Expected 1 argument: root folder path")
    sys.exit(1)

root_folder_path = Path(sys.argv[1])
if not root_folder_path.exists() or not root_folder_path.is_dir():
    print(f"Error - {root_folder_path}, file not found or is not a directory")
    sys.exit(1)

organize_pictures_by_month.main(root_folder_path)
