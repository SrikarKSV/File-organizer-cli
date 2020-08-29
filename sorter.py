from pathlib import Path
from mapped_directories import DIRECTORIES
import shutil


DIRECTORY = Path(__file__).parent / "TEST"

junk_files = [file for file in DIRECTORY.iterdir() if not file.is_dir()]

for file in junk_files:
    file_extension = file.suffix
    for folder in DIRECTORIES:
        extension_list = DIRECTORIES[folder]
        if file_extension in extension_list:
            folder_directory = DIRECTORY / folder
            folder_directory.mkdir(exist_ok=True)
            shutil.move(str(file), str(folder_directory))
