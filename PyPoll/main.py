# Import necessary modules
import os
import csv

# Path to CSV file for reading
csvpath = os.path.join('Resources', 'election_data.csv')

# Read CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Read the header row first
    csvheader = next(csvreader)

# Create variables to store relevant data
    numvotescast = 0

    for row in csvreader:
        numvotescast += 1

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {numvotescast}")
    print("-------------------------")