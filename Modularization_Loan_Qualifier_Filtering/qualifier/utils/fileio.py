"""helper functions to load csv data"""
import csv
from pathlib import Path

# This function loads a CSV file from the filepath defined in `csvpath`


def load_csv(csvpath):
    """reads the csv file from the path provided"""
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


# This function loads a CSV file with the list of banks and available loans information
# from the file defined in `file_path`
def load_bank_data(file_path):
    csvpath = Path(file_path)
    return load_csv(csvpath)
