# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of botes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# import csv

# file_to_load = 'Resources\\election_results.csv'

# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# # To do: perform analysis.
# print(election_data)
# # Close the file.
# election_data.close()

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    # Print the file object.
    
    for row in file_reader:
        print(row)
    headers = next(file_reader)
    print(headers)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as txt_file:

# # Write some data to the file.
#     txt_file.write("Counties in the Election\n------------------------")
# # Write three counties to the file.
#     txt_file.write("\nArapahoe\nDenver\nJefferson")
# # Close the file

# file_to_save.close()