"""
File: organize_pictures_by_month.py
Project: google-takeout-organizer
File Created: Friday, 24th January 2025 10:43:20 am
Author: tonell-m
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path

from alive_progress import alive_bar

TOUCH_T_DATE_FORMAT = "%Y%m%d%H%M"


def main(root_folder_path: Path):
    """
    Script entry point

    Args:
        root_folder_path (Path): Root directory of google takout archive
    """
    # List all metadata file paths
    metadata_filepaths = [
        path
        for path in root_folder_path.rglob("**/*.json")
        if not path.name.startswith(".")  # Ignore hidden files
    ]
    files_count = len(metadata_filepaths)
    print(f"Found {files_count} pictures or videos in folder")

    # Show a little progress bar
    with alive_bar(files_count) as progress_bar:
        # Loop over all metadata files
        for metadata_filepath in metadata_filepaths:
            # Parse json data
            with open(metadata_filepath, "r", encoding="UTF-8") as metadata_file:
                metadata = json.load(metadata_file)

            # Get picture (or video) taken date
            picture_taken_timestamp = int(metadata["photoTakenTime"]["timestamp"])
            picture_taken_date = datetime.fromtimestamp(picture_taken_timestamp)

            # Format that date to the format expected by touch -t
            touch_formatted_date = picture_taken_date.strftime(TOUCH_T_DATE_FORMAT)
            # print(f"{picture_taken_date} -> {touch_formatted_date}")

            # Get filepath of the picture (or video) itself. To do this we get just the stem
            # (filename without .json extension) and append it to the parent directory
            picture_filepath = metadata_filepath.parent / metadata_filepath.stem
            # Check that picture file exists because sometimes the metadata still exists with
            # the picture actually being deleted
            if not picture_filepath.exists():
                continue

            # Run touch -t to update creation and modificaiton date of the picture file
            subprocess.run(
                [
                    "touch",
                    "-am",
                    "-t",
                    touch_formatted_date,
                    str(picture_filepath.absolute()),
                ],
                check=True,
            )
            progress_bar()  # pytlint:disable not-callable

    # Once all files metadata have been successfully updated, get rid of all the JSON files
    for path in metadata_filepaths:
        path.unlink()
