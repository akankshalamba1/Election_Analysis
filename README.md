# Election_Analysis
Election-Analysis is based on the Colorado board of elections, where we used Python software to help, Tom, audit the tabulated results for a U.S. congressional precinct in Colorado. Our task included the following:
- Reporting the total number of votes cast
- Each county and its total vote count of votes
- Each county and its percentage of the total votes
- The county with the largest number of voters
- The percentage of votes for each candidate
- The total number of votes for each candidate 
- The winner of the election based on the popular vote
The output of the election results need to be printed on the terminal as well as a text file.

## Overview of Election Audit
In the Election Audit we used the dataset with three columns Ballot ID, County, Candidate and 369712 rows of election results in three county Jefferson,Denver and Arapahoe. There are three candidates running the election Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane. In this challenge we used two lists candiate_options and county and two dictionaries candidate_votes and county_votes.

![step1](https://user-images.githubusercontent.com/111251560/190280131-fc709a3f-41a0-4861-81f0-867ad07e0b23.png)

winning_candidate and winning_county variables are initalized and winning count, winning percentage, winning_county, winning_county_percentage are initalized to 0 as they will be containing numeric values as shown above. 
As we are required to provide output on terminal and output on text file so we assign the path of the csv file to a variable file_to_load and the text file we want to print the elections output to as file_to_save


## Election-Audit Results
- **How many votes were cast in this congressional election?**
- **Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.**
- **Which county had the largest number of votes?**
- **Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.**
- **Which candidate won the election, what was their vote count, and what was their percentage of the total votes?**
## Election-Audit Summary
