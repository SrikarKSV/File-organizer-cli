from pathlib import Path
import pathlib
from mapped_directories import EXTENSIONS
import shutil
import argparse
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(message)s")

parser = argparse.ArgumentParser(
    description="Organize the files in a folder into their respective category"
)

parser.add_argument(
    "-d",
    "--directory",
    help="Enter the absolute path(inside quotes) of the directories, give space between each path if given multiple",
    type=str,
    metavar="",
    nargs="+",
)

parser.add_argument(
    "-e",
    "--exclude",
    help="Will exclude the given extensions from sorting, give space between each extension if given multiple",
    type=str,
    metavar="",
    nargs="+",
    default=["Empty"],
)

parser.add_argument(
    "-i",
    "--input",
    help="Specify a text file with the paths to the dirctories line by line(Won't work if --directory given)",
    type=str,
    metavar="",
)

parser.add_argument(
    "-l",
    "--log",
    help="The moved files and destination will be logged in the terminal",
    action="store_true",
)

args = parser.parse_args()


def get_directories():
    if args.directory:
        return args.directory
    elif args.input:
        input = args.input
    else:
        raise Exception("--directory or --input either not given, specify a directory")
        sys.exit()

    input_file = pathlib.Path(input)
    assert input_file.exists(), f"No text file with name {input_file.name}"

    directories = []
    with open(input_file, encoding="utf-8") as f:
        for directory in f:
            directories.append(directory.strip())

    return directories


def organize_files():
    directories = get_directories()
    for path in directories:
        DIRECTORY = Path(path)
        assert DIRECTORY.exists(), "Wrong path provided"
        unorganized_files = [file for file in DIRECTORY.iterdir() if file.is_file()]

        for i, file in enumerate(unorganized_files):
            unorganized_file_extension = file.suffix
            if unorganized_file_extension not in args.exclude:
                for folder in EXTENSIONS:
                    extension_list = EXTENSIONS[folder]
                    if unorganized_file_extension in extension_list:
                        folder_directory = DIRECTORY / folder
                        folder_directory.mkdir(exist_ok=True)
                        try:
                            shutil.move(str(file), str(folder_directory))
                            if args.log:
                                logging.debug(f"{file.name} is moved to {folder}")
                        except shutil.Error as e:
                            logging.debug(e)


if __name__ == "__main__":
    organize_files()