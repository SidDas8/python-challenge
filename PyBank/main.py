# Import necessary modules
import os
import csv

# Path to CSV file for reading
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Read the header row first
    csvheader = next(csvreader)
    
# Create variables to store relevant data

    # We must read the first row of data before the loop, because the calculation 
    # for average monthly change and greatest change must begin from the second row
    firstline = next(csvreader)
    firstmonthdate = firstline[0]
    firstmonthamount = int(firstline[1])

    # First month is equal to 1 instead of 0 because the loop starts at the second row
    numberofmonths = 1
    
    # Calculation for net amount must include first month's data
    netprofitorloss = firstmonthamount

    # Create lists to track changes and date in "Profit/Losses" over the entire period
    dateformonthlychange = []
    listformonthlychange = []

    # Loop through csv file
    for row in csvreader:

        # Total number of months included in the data set
        numberofmonths += 1

        # Total amount of "Profit/Losses" over the entire period
        netprofitorloss += int(row[1])

        # Average changes in "Profit/Losses" over the entire period
        # Find monthly change and append to relevant list
        monthlychange = int(row[1]) - firstmonthamount
        listformonthlychange.append(monthlychange)
        # Set current month's amount as previous month's amount to be used for the next iteration of the loop
        firstmonthamount = int(row[1])

        # Track dates for greatest increase and greatest decrease of profits
        dateformonthlychange.append(row[0])

    # After both lists are full of data, create variables to track the month and amount for the 
    # greatest increase and greatest decrease, starting with the first change in profits/losses
    greatestincrease = listformonthlychange[0]
    greatestdecrease = listformonthlychange[0]
    dateofincrease = dateformonthlychange[0]
    dateofdecrease = dateformonthlychange[0]
    
    # Loop through list of monthly changes
    for change in range(len(listformonthlychange)):
        # Greatest increase
        if int(listformonthlychange[change]) > greatestincrease:
            greatestincrease = int(listformonthlychange[change])
            dateofincrease = dateformonthlychange[change]

        # Greatest decrease
        if int(listformonthlychange[change]) < greatestdecrease:
            greatestdecrease = int(listformonthlychange[change])
            dateofdecrease = dateformonthlychange[change]


    # Calculate monthly change per month
    averagemonthlychange = round(sum(listformonthlychange) / len(listformonthlychange), 2)
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {numberofmonths}")
    print(f"Total: ${netprofitorloss}")
    print(f"Average Change: ${averagemonthlychange}")
    print(f"Greatest Increase in Profits: {dateofincrease} (${greatestincrease})")
    print(f"Greatest Decrease in Profits: {dateofdecrease} (${greatestdecrease})")

# Write CSV file
outputpath = os.path.join('analysis', 'analysis.txt')

with open(outputpath, 'w', newline='') as outputfile:
    
    csvwriter = csv.writer(outputfile, delimiter=',')

    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow("----------------------------")
    csvwriter.writerow(f"Total Months: {numberofmonths}")
    csvwriter.writerow(f"Total: ${netprofitorloss}")
    csvwriter.writerow(f"Average Change: ${averagemonthlychange}")
    csvwriter.writerow(f"Greatest Increase in Profits: {dateofincrease} (${greatestincrease})")
    csvwriter.writerow(f"Greatest Decrease in Profits: {dateofdecrease} (${greatestdecrease})")