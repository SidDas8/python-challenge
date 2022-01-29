# Read CSV file

# Import necessary modules
import os
import csv

from sympy import li

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Read the header row first
    csvheader = next(csvreader)
    
# Create variables to store relevant data

    # We must read the first row before the loop because the calculation for monthly change must begin from the second row
    firstline = next(csvreader)
    firstmonthamount = int(firstline[1])

    # First month is equal to 1 instead of 0 because the loop starts at the second row
    numberofmonths = 1
    
    # Calculation for net amount must include first month's data
    netprofitorloss = firstmonthamount

    # Create lists to track average changes in "Profit/Losses" over the entire period
    listformonthlychange = []

    for row in csvreader:

        # Calculate total number of months included in the data set
        numberofmonths += 1

        # Calculate total amount of "Profit/Losses" over the entire period
        netprofitorloss += int(row[1])

        # Calculate average changes in "Profit/Losses" over the entire period
        monthlychange = int(row[1]) - firstmonthamount
        listformonthlychange.append(monthlychange)
        firstmonthamount = int(row[1])


    # Calculate monthly change per month
    averagemonthlychange = round(sum(listformonthlychange) / len(listformonthlychange), 2)
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {numberofmonths}")
    print(f"Total: ${netprofitorloss}")
    print(f"Average Change: ${averagemonthlychange}")