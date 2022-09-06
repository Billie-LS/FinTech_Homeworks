# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.
This contains a helper function for loading and saving CSV files.
"""
# required imports for operation of module functions
import csv
from pathlib import Path
import questionary


# This function loads a CSV file from the filepath defined in `csvpath`
# will utilize import csv
def load_csv(csvpath):
    """Reads the CSV file from path provided.
    Args:
        csvpath (Path): The csv file path.
    Returns:
        A list of lists that contains the rows of data from the CSV file.
    """
    with open(csvpath, "r") as csvfile:
        data = []   # create empty set
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV and add into empty set via .append() function
        for row in csvreader:
            data.append(row)
    return data


# This function loads a CSV file with the list of banks and available loans information
# from the file path provided by user via command line interface (CLI)
# via questionary.text().ask() function, for the purpose of this function,
# at prompt for CSV file path, user should enter  ./data/daily_rate_sheet.csv
# will utilize imports csv, Path, and questionary
def input_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.
    Returns:
        The bank data from the data rate sheet CSV file.
    """
    csvpath = questionary.text(
        "Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)

    # hard exit should the user enter the incorrect path, with feedback
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


# This function opens a new CSV path for saving the generated list of
# pre-qualified banks and loans via creating a csv writer to enable
# saving the list by creating/writing the data into a new csv file
# a header for column labels is indicated
def save_csv(csvpath, data):
    """Reads the CSV file from path provided.
    Args:
        csvpath (Path): The csv file path.
    Returns:
        A list of lists that contains the rows of data from the CSV file.
    """
    # creates new csv read and write path
    with open(csvpath, "r+", newline='') as csvfile:
        # create new csv writer
        csvwriter = csv.writer(csvfile, delimiter=",")
        header = ['Lender', 'Max Loan Amount', 'Max LTV',
                  'Max DTI', 'Min Credit Score', 'Interest Rate']
        if header:
            # add header to new csv file
            csvwriter.writerow(header)
        # inputs data in each row of new csv file
        csvwriter.writerows(data)
