import csv
import os
from datetime import datetime

INPUT_FILE = "/data/input/students.csv"
OUTPUT_FILE = "/data/output/results.txt"

print("=" * 50)
print("SWE40006 Docker Data Processing Service")
print("=" * 50)
print("Container started successfully.")
print(f"Reading input file: {INPUT_FILE}")

os.makedirs("/data/output", exist_ok=True)

marks = []

try:
    with open(INPUT_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            marks.append(float(row["mark"]))

    if marks:
        total_records = len(marks)
        average = sum(marks) / total_records
        highest = max(marks)
        lowest = min(marks)

        with open(OUTPUT_FILE, "w") as file:
            file.write("SWE40006 Data Processing Results\n")
            file.write("=" * 35 + "\n")
            file.write(f"Records processed: {total_records}\n")
            file.write(f"Average mark: {average:.2f}\n")
            file.write(f"Highest mark: {highest:.2f}\n")
            file.write(f"Lowest mark: {lowest:.2f}\n")
            file.write(f"Processed at: {datetime.now()}\n")

        print(f"Records processed: {total_records}")
        print(f"Average mark: {average:.2f}")
        print(f"Highest mark: {highest:.2f}")
        print(f"Lowest mark: {lowest:.2f}")
        print(f"Results written to: {OUTPUT_FILE}")
        print("Processing completed successfully.")

    else:
        print("No records were found.")

except Exception as error:
    print(f"Processing failed: {error}")
    raise