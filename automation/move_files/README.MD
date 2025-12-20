# move_files.py

This Python script moves one or more files to a specified destination folder.  
It is designed for small automation tasks, such as organizing files quickly and safely.

---

## Features
- Move multiple files in one command
- Automatically creates the destination folder if it does not exist
- Logs all actions to `movingfiles.log`
- Displays warnings in the console for missing files
- Safe, reusable, and professional for client use

---

## Usage

From the command line, run:

```bash
python move_files.py <file1> <file2> ... <destination>
```
---
## Example:
- python move_files.py report1.csv report2.csv archive_folder
- This moves report1.csv and report2.csv into the folder archive_folder.
- If archive_folder does not exist, it will be created automatically.
- Any missing files will trigger a console warning but will not stop the script.

---

## Log File

All actions are recorded in movingfiles.log in the same folder as the script.
This includes:

- Which files were successfully moved
- Any warnings for missing files
- Creation of the destination folder
- Requirements

---

## Python 3.x

- Standard libraries only: shutil, os, sys, logging

---

## Notes

- Designed for automation and small repetitive tasks.
- Can be easily extended for more advanced file management tasks.