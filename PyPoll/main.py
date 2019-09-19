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

# initialize the winner
winner = ""
winner_votes= 0

# set the path for the txt file
output_path= os.path.join("Outputs", "PyPoll_output.txt")

# open the file
with open (output_path, 'w', newline='') as textfile:
    
    # print to the terminal
    print("election results")
    print("---------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------")
    
    # write to the file
    textwriter=textfile.write("election results\n")
    textwriter=textfile.write("---------------------------\n")
    textwriter=textfile.write(f"Total Votes: {total_votes}\n")
    textwriter=textfile.write("---------------------------\n")

    # loop through the candiates    
    for candidate in candidate_dict:
        votes = candidate_dict[candidate]
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes
        print(f"{candidate}: {round(float(votes/total_votes*100),3)}% ({votes})")

        #write to the file
        textwriter=textfile.write(f"{candidate}: {round(float(votes/total_votes*100),3)}% ({votes})\n")

    print("---------------------------")
    print(f"winner: {winner}")
    print("---------------------------")

    # write to the file
    textwriter = textfile.write("---------------------------\n")
    textwriter = textfile.write(f"winner: {winner}\n")
    textwriter = textfile.write("---------------------------\n")




