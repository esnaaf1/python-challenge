# main.pay in PyPoll
# Farshad Esnaashari
# Data Anlytics and Visualization M-W

# import packages
import os
import csv

# Set the path for the csv file
election_data_csv = os.path.join("Resources", "election_data.csv")

# create a dictionary placeholder

candidate_dict = {}

# open the data file
with open (election_data_csv, newline = "") as csvfile:

# read the data 
    csvreader = csv.reader(csvfile, delimiter=",")

    # read the header
    csv_header = next(csvreader)
    # inialize the total voites
    total_votes = 0
    # loop through the data file
    for row in csvreader:
        candidate = row[2]
        total_votes +=1

        # if the candidate is in the dictionary add to vote count
        if candidate in candidate_dict:
            vote = candidate_dict.get(candidate)
            vote +=1
            candidate_dict[candidate] = vote
        # otherwise add the candidate and set the vote to 1
        else:
            candidate_dict[candidate] = 1
print(f" total: {total_votes}")
for candidates, votes in candidate_dict.items():
    print (candidates, votes)


# 
# while answer =="y":
#     candidate = input("Enter the Candidate Name:  ")

#     print(f" from the keyboard: { candidate}")

#     # if the candidate is the dictionary, then increment the voote
#     if candidate in candidate_dict:
#         vote = candidate_dict.get(candidate)
#         vote +=1 
#         candidate_dict[candidate] = vote
#     else:
#         candidate_dict[candidate] = 1
#     answer = input("Do you want to add another Candidate? y(es) or n(o)? ")
# print(f" candidate_dict { candidate_dict}")