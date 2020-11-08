import argparse
import logging
from organize_files.organize import OrganizeFiles

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s: %(message)s")

parser = argparse.ArgumentParser(
    prog="Organize files",
    description="Organize the files in a folder into their respective category",
    epilog="If you want to see some examples then visit: https://github.com/SrikarKSV/File-organizer-cli",
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
    help="Will exclude the given extensions from sorting, give a comma-separated list of extensions(No spaces)",
    type=str,
    metavar="",
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


if __name__ == "__main__":
    files = OrganizeFiles(args)
    files.organize_files()
