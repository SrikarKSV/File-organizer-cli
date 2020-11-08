from organize_files.mapped_directories import EXTENSIONS
from pathlib import Path
import shutil
import logging


class OrganizeFiles:
    """
    A class used to organize files in a folder.

    Predifined extensions are mapped to their category and new extensions
    can be added to the list.

    Attributes
    ----------
    args : object
        contains the arguments enterin in cli.

    excluded_extenxions: list
        list of excluded extensions.

    Methods
    -------
    get_directories
        Parses the given directories from the arguments.

    organize_files
        Organizes the files into their categories.
    """

    def __init__(self, args) -> None:
        self.args = args
        self.excluded_extenxions = self.parse_excluded_extension()

    def get_directories(self) -> list:
        """
        Parses the list of directories from the arguments.

        The arguments must be inside double quotes and a space
        should be given if multiple are provided.

        Raises
        ------
        FileNotFoundError
            If no directory or input text file containing directories
            are provided.
        """
        if self.args.directory:
            return self.args.directory
        elif self.args.input:
            input = self.args.input
        else:
            raise FileNotFoundError(
                "--directory or --input either not given, specify a directory"
            )

        input_file = Path(input)
        assert input_file.exists(), f"No text file with name {input_file.name}"

        directories = []
        with open(input_file, encoding="utf-8") as f:
            for directory in f:
                directories.append(directory.strip())

        return directories

    def organize_files(self) -> None:
        """
        Organizes the files inside the given directories into their respective
        directories.
        """
        directories = self.get_directories()
        for path in directories:
            DIRECTORY = Path(path)
            assert DIRECTORY.exists(), "Given directory path does not exist"
            # Getting all the files from the specified folder
            unorganized_files = [file for file in DIRECTORY.iterdir() if file.is_file()]

            for file in unorganized_files:
                unorganized_file_extension = file.suffix
                if unorganized_file_extension in self.excluded_extenxions:
                    continue
                for folder in EXTENSIONS:
                    extension_list = EXTENSIONS[folder]
                    if unorganized_file_extension in extension_list:
                        folder_directory = DIRECTORY / folder
                        folder_directory.mkdir(exist_ok=True)
                        try:
                            shutil.move(str(file), str(folder_directory))
                            if self.args.log:
                                logging.debug(f"{file.name} is moved to {folder}")
                        except shutil.Error as e:
                            logging.debug(e)

    def parse_excluded_extension(self) -> list:
        """
        Parses the comma-separated list of extension from the argument.

        These extensions will not be sorted.
        """
        if not self.args.exclude:
            return ["EMPTY"]
        excluded_extenxions = self.args.exclude.split(",")
        return excluded_extenxions
