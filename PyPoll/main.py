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

    # Create variable to track winner
    winnervotes = votespercandidate[0]
    winnername = candidates[0]
    
    for index in range(len(votespercandidate)):
        
        # Find percentage of votes each candidate won
        percent = round((votespercandidate[index] / numvotescast) * 100, 3)
        percentagevotes.append(percent)

        # Find the winner of the election
        if votespercandidate[index] > winnervotes:

            winnername = candidates[index]

    # Print out results to terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {numvotescast}")
    print("-------------------------")
    for each in range(len(candidates)):
        print(f"{candidates[each]}: {percentagevotes[each]}% ({votespercandidate[each]})")
    print("-------------------------")
    print(f"Winner: {winnername}")
    print("-------------------------")
    
# Path to CSV file for writing
outputpath = os.path.join('analysis', 'electiondata_analysis.txt')

# Write CSV file
with open(outputpath, 'w', newline='') as outputfile:

    outputfile.write("Election Results\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Total Votes: {numvotescast}\n")
    outputfile.write("-------------------------\n")
    for each in range(len(candidates)):
        outputfile.write(f"{candidates[each]}: {percentagevotes[each]}% ({votespercandidate[each]})\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Winner: {winnername}\n")
    outputfile.write("-------------------------\n")