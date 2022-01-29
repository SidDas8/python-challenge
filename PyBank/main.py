# Read CSV file

# The os module will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Read the header row first (skip this step if there is now header)
    csvheader = next(csvreader)
    print(f"Header: {csvheader}")