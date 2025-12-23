# CSV Cleaner & Standardizer

A Python automation script that cleans and standardizes CSV files by validating headers, normalizing data formats, and removing incomplete records.

This script is designed as a **reliable, production-style data cleaning utility**, suitable for automation workflows and freelance data-processing tasks.

---

## ✨ Features

- Validates input arguments and file existence
- Accepts **CSV files only**
- Enforces required headers:
  - `name`
  - `email`
  - `country`
- Normalizes data:
  - Names → Title Case
  - Emails → Lowercase
  - Countries → Title Case
- Skips incomplete rows safely
- Writes clean output to a new CSV file
- Logs all operations and errors to a log file

---

## 📌 Requirements

- Python 3.8+
- Standard library only (no external dependencies)

---

## 🚀 Usage

```bash
python csv_cleaner.py input.csv output.csv
```
---

## Example
python csv_cleaner.py raw_data.csv cleaned_data.csv

---

## 📂 Expected CSV Format

Input CSV must contain the following headers (case-insensitive):
name,email,country
Rows missing any of these values will be skipped.

---
## 📝 Logging

All actions are logged to:
cleaner.log
- The log includes:
- Validation errors
- Header mismatches
- Skipped rows
- Processing summary (rows read / written / skipped)

---
##⚠️ Error Handling

The script will exit with an error if:

- Incorrect number of arguments is provided
- Input file does not exist
- File is not a .csv
- Required headers are missing
- Input file is empty

---

## 🎯 Purpose

This script is part of a growing Python Automation portfolio, focusing on:

- File-based automation
- Data validation
- Clean logging practices
- Real-world usability
