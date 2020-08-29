from pathlib import Path
from mapped_directories import DIRECTORIES
import shutil
import argparse

parser = argparse.ArgumentParser(
    description="Organize the files in a folder into their respective category"
)

parser.add_argument(
    "-d",
    "--directory",
    help="Enter the absolute path(inside quotes) of the directories, give space between each path if given multiple",
    type="str",
    required=True,
    metavar="",
    nargs="+",
)

parser.add_argument(
    "-e",
    "--exclude",
    help="Will exclude the given extensions from sorting, give space between each extension if given multiple",
    type="str",
    metavar="",
    nargs="+",
)

args = parser.parse_args()


def organize_files():
    for path in args.directory:
        DIRECTORY = Path(path)
        assert DIRECTORY.exists(), "Wrong path provided"
        unorganized_files = [file for file in DIRECTORY.iterdir() if file.is_file()]

        for file in unorganized_files:
            unorganized_file_extension = file.suffix
            if unorganized_file_extension not in args.exclude:
                for folder in DIRECTORIES:
                    extension_list = DIRECTORIES[folder]
                    if unorganized_file_extension in extension_list:
                        folder_directory = DIRECTORY / folder
                        folder_directory.mkdir(exist_ok=True)
                        shutil.move(str(file), str(folder_directory))


if __name__ == "__main__":
    organize_files()