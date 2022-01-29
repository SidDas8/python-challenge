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

    # List for name of candidates
    candidates = []

    # Track the number of votes per candidate using the index from list of candidates
    votespercandidate = []

    # Track the percentage of votes won per candidate
    percentagevotes = []

    # Loop through CSV file
    for row in csvreader:
        
        # Count number of votes
        numvotescast += 1

        # If name is not already in list of candidate names
        if row[2] not in candidates:
        
            # Add name to the candidate names' list
            candidates.append(row[2])

            # Begin tracker to keep track of the number of votes for candidate
            votespercandidate.append(0)

        # Find index of candidate name
        votesindex = candidates.index(row[2])

        # Add vote to index of candidate
        votespercandidate[votesindex] += 1

    # Find percentage of votes each candidate won
    for index in range(len(votespercandidate)):
        
        percent = round((votespercandidate[index] / numvotescast) * 100, 3)

        percentagevotes.append(percent)


    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {numvotescast}")
    print("-------------------------")
    print(candidates)
    print(votespercandidate)
    print(percentagevotes)