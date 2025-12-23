"""
move_files.py

Move multiple files to a specified destination folder.

Usage:
    python move_files.py <file1> <file2> ... <destination>

Logs all actions to movingfiles.log
"""

import shutil
import os
import sys
import logging

logging.basicConfig(
   filename="movingfiles.log",
   level=logging.INFO,
   format="%(asctime)s - %(levelname)s - %(message)s",
   )

def main():

    if len(sys.argv) <= 2:
        logging.warning("Usage: python move_files.py <file1> <file2> ... <destination>")
        sys.exit()

    file_names = sys.argv[1:-1]
    logging.info("files ready to be moved")

    destination = sys.argv[-1]

    c_folder = os.getcwd()

    if not os.path.exists(destination):
        os.makedirs(destination)
        logging.info(f"Created destination folder: {destination}")

    count = 0
    for name in file_names:
        name = name.strip()
        src_ = os.path.join(c_folder, name)
        des = os.path.join(destination, name)

        if not os.path.isfile(src_) and not os.path.isdir(src_):
            logging.warning(f"Source file not found: {src_}")
            print(f"Source file not found: {src_}")
            continue

        try:
            shutil.move(src_, des)
            count += 1
            logging.info(f"{name} has been moved from {src_} to {des} successfully")
        except FileNotFoundError:
            continue

    logging.info(f"Finished moving files. Successfully moved {count} files.")


if __name__ == "__main__":
    main()
