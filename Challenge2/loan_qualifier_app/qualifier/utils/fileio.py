# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path
import questionary
# This function loads a CSV file from the filepath defined in `csvpath`


def load_csv(csvpath):
    """Reads the CSV file from path provided.
    Args:
        csvpath (Path): The csv file path.
    Returns:
        A list of lists that contains the rows of data from the CSV file.
    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def input_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.
    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text(
        "Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def save_csv(csvpath, data):
    """Reads the CSV file from path provided.
    Args:
        csvpath (Path): The csv file path.
    Returns:
        A list of lists that contains the rows of data from the CSV file.
    """
    with open(csvpath, "r+", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        header = ['Lender', 'Max Loan Amount', 'Max LTV',
                  'Max DTI', 'Min Credit Score', 'Interest Rate']
        if header:
            csvwriter.writerow(header)
        csvwriter.writerow(data)
