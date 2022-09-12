# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of botes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")
# Open the election results and read the file.
file_to_save = os.path.join("winner", "winning_candidate_analysis.txt")

total_votes = 0
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

candidate_option = []

candidate_votes = {}
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    # Print the file object.
    
    # for row in file_reader:
    #     print(row)
    headers = next(file_reader)
    # print(headers)

    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]
     
        if candidate_name not in candidate_option:
           
            candidate_option.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
    
        candidate_votes[candidate_name] += 1 

with open(file_to_save, "w") as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"Vote counts:\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        vote_per_cand = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(vote_per_cand)
        txt_file.write(vote_per_cand)
    # Determine winning vote count and candidate    
    # 1. Determine if the votes are greater than the winning count.

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------")
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary) 