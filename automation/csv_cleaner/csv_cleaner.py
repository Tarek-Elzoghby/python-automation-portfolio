"""
csv_cleaner.py

Clean and standardize CSV data.

Expected headers:
    name, email, country

Usage:
    python csv_cleaner.py input.csv output.csv

Logs all actions to csv_cleaner.log
"""
import csv
import sys
import logging
from pathlib import Path

logging.basicConfig(
    filename="cleaner.log",
    level=logging.INFO,
    format="%(asctime)s, %(levelname)s, %(message)s",
)


def main():
    # Argument validation
    if len(sys.argv) != 3:
        logging.error("Usage: python cleaner.py <input.csv> <output.csv>")
        print("Usage: python data_cleaner.py <input.csv> <output.csv>")
        sys.exit(1)

    file_input = Path(sys.argv[1])
    file_output = Path(sys.argv[2])

    if not file_input.exists():
        logging.error("Input file does not found")
        print("Input file does not found")
        sys.exit(1)

    if file_input.suffix.lower() != ".csv" or file_output.suffix.lower() != (".csv"):
        logging.error("the program excpects only csv files")
        print("your files is not a csv file")
        sys.exit(1)

    headerslist = {"name", "email", "country"}

    with open(file_input, "r") as rfile, open(file_output, "w", newline="") as wfile:
        reader = csv.DictReader(rfile)
        if not reader.fieldnames:
            logging.error("Missing required headers")
            sys.exit(1)

        normalized_headers = {header.strip().lower() for header in reader.fieldnames}
        if not headerslist.issubset(normalized_headers):
            logging.error(f"Missing required headers: {reader.fieldnames}")
            print("Error: CSV is missing required headers")
            sys.exit(1)

        logging.info("the input file is ready and the headers is checked ")

        writer = csv.DictWriter(wfile, fieldnames=["name", "email", "country"])
        writer.writeheader()
        count = 0

        total_rows = 0
        written_rows = 0
        skipped_rows = 0

        for row in reader:
            total_rows += 1

            name = row.get("name", "").strip()
            email = row.get("email", "").strip()
            country = row.get("country", "").strip()

            if not name or not email or not country:
                skipped_rows += 1
                logging.warning(f"Skipped incomplete row: {row}")
                continue

            writer.writerow(
                {
                    "name": name.title(),
                    "email": email.lower(),
                    "country": country.title(),
                }
            )
            written_rows += 1

    logging.info("CSV cleaning completed successfully")
    logging.info(f"Total rows read: {total_rows}")
    logging.info(f"Rows written: {written_rows}")
    logging.info(f"Rows skipped: {skipped_rows}")



if __name__ == "__main__":
    main()
