from pathlib import Path
from mapped_directories import DIRECTORIES
import shutil
import argparse

parser = argparse.ArgumentParser(
    description="Sort the files in a folder into their respective category"
)

parser.add_argument(
    "-d",
    "--directory",
    help="Enter the absolute path(inside quotes) of the directory with the unorganized files",
    required=True,
    metavar="",
)

args = parser.parse_args()


def organize_files():
    DIRECTORY = Path(args.directory)
    unorganized_files = [file for file in DIRECTORY.iterdir() if file.is_file()]

    for file in unorganized_files:
        unorganized_file_extension = file.suffix
        for folder in DIRECTORIES:
            extension_list = DIRECTORIES[folder]
            if unorganized_file_extension in extension_list:
                folder_directory = DIRECTORY / folder
                folder_directory.mkdir(exist_ok=True)
                shutil.move(str(file), str(folder_directory))


if __name__ == "__main__":
    organize_files()