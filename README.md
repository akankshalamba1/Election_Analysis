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
Following dataset was used for this analysis:

[Election_results](/resources/election_results.csv)

## Overview of Election Audit
In the Election Audit we used the dataset with three columns Ballot ID, County, Candidate and 369712 rows of election results in three county Jefferson,Denver and Arapahoe. There are three candidates running the election Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane. In this challenge we used two lists candiate_options and county and two dictionaries candidate_votes and county_votes.

![step1](https://user-images.githubusercontent.com/111251560/190280131-fc709a3f-41a0-4861-81f0-867ad07e0b23.png)

winning_candidate and winning_county variables are initalized and winning count, winning percentage, winning_county, winning_county_percentage are initalized to 0 as they will be containing numeric values as shown above. 

As we are required to provide output on terminal and output on text file so we assign the path of the csv file to a variable file_to_load and the text file we want to print the elections output to as file_to_save. 

**For loops and Conditional statements**
For this Analysis we used 3 for loops:
- *To find the total number of votes* 

 ![for1](https://user-images.githubusercontent.com/111251560/190293653-10c75913-e595-4104-b2ad-de9c77c0b609.png)

- *To find the total votes and percentage of votes from each county and Largest County turnover*

![for2](https://user-images.githubusercontent.com/111251560/190293673-b8861cc6-02fc-48e5-8680-88bf44a45a02.png)

- *To find the total votes and percentage of votes each candidate got and the winning candidate*

![for3](https://user-images.githubusercontent.com/111251560/190294031-afd62a54-8ce2-46bf-875f-bc0dcb7bcf51.png)

With the used of for loop and If statements in Python we were able to get our results as requested by Tom and his boss Seth.

## Election-Audit Results
- **How many votes were cast in this congressional election?**

Total 369,711 votes were casted

- **Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.**

*County Votes:*
- Jefferson: 38,855 votes were casted which is, 10.5% of the total votes casted
- Denver: 306,055 votes were casted which is 82.8% of the total votes casted
- Arapahoe: 24,801 votes were casted which is 6.7% of the total votes casted

- **Which county had the largest number of votes?**

Dever county had the largest number of votes casted (306,055 votes) 82.8%

- **Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.**

- Charles Casper Stockham received 85,213 votes, 23.0% of total votes
- Diana DeGette received 272,892 votes, 73.8% of total votes
- Raymon Anthony Doane received 11,606 votes, 3.1% of total votes

- **Which candidate won the election, what was their vote count, and what was their percentage of the total votes?**

> -------------------------
> Winner: Diana DeGette
---------------------------
> Winning Vote Count: 272,892
---------------------------
> Winning Percentage: 73.8%
---------------------------

![Test Image](/resources/Election_result_terminal.png)

![election_results_textfile_output](https://user-images.githubusercontent.com/111251560/190309112-ff1bb9df-ab34-48ec-9862-4a7b87983a81.png)

## Election-Audit Summary

We would like to initaite a business proposal to the election commission that our script could be used to provide election results for any elections. By working pon this challenege we were able to create a script that could be used by election commission to summarize any election results. 
The business proposal is attached here with:

[business proposal.pdf](https://github.com/akankshalamba1/Election_Analysis/files/9571449/business.proposal.pdf)
![business_proposal](https://user-images.githubusercontent.com/111251560/190305630-4e6bde66-c1da-473a-a9d4-f2c14b142cc1.png)

**Proposaed modifications to the script:**
- The script used in analysis of election results in Colorado already has standadized variable names like winning_candidate, winning_county, winning_percentage that could remain the same for any election result data. It could be used for local and higher level elections as well which have more number of county and vast number of candidate. the output will update based on the different attributes provided in the data. we could modify the script to just show the winning candiate, total votes and vote of each candidate if the election is at a smaller level by using the code attached below:

![winning_candidate](https://user-images.githubusercontent.com/111251560/190295610-272fe547-c5bd-4d21-8141-6616695641ac.png)
[Pypoll](/resources/Pypoll.py)

- For the election at a larger level we could further refcator the code and provide data by different county or province with how many votes each candidate get in each county. This output will be helpful in Federal election were it will show which candidate got the most votes in which province. 

> For example: 
> Denver : 
- 1. Charles Casper Stockham got __ votes
- 2. Diana DeGette got __ votes
- 3. Raymon Anthony Doane got __ votes

> Jefferson :
- 1. Charles Casper Stockham got __ votes
- 2. Diana DeGette got __ votes
- 3. Raymon Anthony Doane got __ votes

> Arapahoe :
- 1. Charles Casper Stockham got __ votes
- 2. Diana DeGette got __ votes
- 3. Raymon Anthony Doane got __ votes

There are ways this script could be modified based on the output that we need from it. If given opportunity our method of audit will be of great use for the Election commission.
