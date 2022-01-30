# python-challenge


# PyBank

* The first step is to read the CSV file with the budget data

* Read the header and first row of data before beginning the loop

* Before the loop, read the first row because the calculation for 
* average monthly change and greatest change uses data from the first row

* Create necessary variables and lists
* The variables must account for starting the loop from the second row

* Looping through the CSV file, calculate the total number of months and the net amount of profit or losses

* In addition, track the date and amount for all the monthly changes in a list

* Once the monthly change lists are full of dates and amounts, loop through either list to find 
* the greatest increase, greatest decrease, and associated month

* Calculate the average monthly change in profits/losses

* Finally, print the information in the terminal and an exported text file


# PyPoll

* The first step is to read the csv file with the budget data

* Read the header before beginning the loop

* Create necessary variables and lists
* Use 3 lists to hold the names of the candidates, 
* the number of votes per candidate, and the percentage of votes per candidate

* NOTE: Since each list is the same length, the index of each list correlates to each candidate
* NOTE: Tried to use a set to avoid duplicate names of candidates but it didn't work
* because but sets are unordered so we cannot use the index for correlation

* Looping through the CSV file, track the total number of votes, 
* the names of the candidates, and the number of votes per candidate
* NOTE: Use the index to add a vote to the correct candidate

* After the lists are completely full of relevant data, loop through the votes per candidate list 
* to find the percentage of votes for each candidate and the highest vote count

* Use the index to find the name of the candidate with the most votes

* Finally, print the information in the terminal and an exported text file