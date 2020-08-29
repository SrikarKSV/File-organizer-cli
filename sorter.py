import os
from pathlib import Path
from pprint import pprint
from mapped_directories import DIRECTORIES


DIRECTORY = Path(__file__).parent / "TEST"

files = [file for file in DIRECTORY.iterdir()]

for file in files:
    extension = file.suffix
    print(extension)