# Modules
import os
import csv
agains = "y"

total_votes = 0
total = 0
changes = 0
high_months = " "
low_months = " "
high = 0
low = 0
names = 0
mostest = 0
hold = 0
winner = " "

candidates = []
candidate_votes = []

# Set path for file
csvpath = os.path.join("election_data.csv")

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        csv_header = next(csvreader)

    # Loop through looking for the video
        for row in csvreader:
                total_votes= total_votes + 1
                if row[2] not in candidates:
                    candidates.append(row[2])
                    candidate_votes.append(0)
                votes = candidates.index(row[2])
                candidate_votes[votes] = candidate_votes[votes] + 1

print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------")
for names in range(len(candidate_votes)):
    percent = candidate_votes[names]/total_votes
    print(f"{candidates[names]}: {round(percent*100, 3)}% ({candidate_votes[names]})")
print(f"--------------------------")
for highest in range(len(candidate_votes)):
    if mostest < candidate_votes[highest]:
        mostest = candidate_votes[highest]

hold = candidate_votes.index(mostest)
winner = candidates[hold]

print(f"Winner: {winner}")
print(f"--------------------------")

txtpath = os.path.join("..","..","Analysis","Analysis_Poll.txt")

with open(txtpath, 'w') as f:
    f.write(f"Election Results")
    f.write('\n'f"--------------------------")
    f.write('\n'f"Total Votes: {total_votes}")
    f.write('\n'f"--------------------------")
    for names in range(len(candidate_votes)):
        percent = candidate_votes[names]/total_votes
        f.write('\n'f"{candidates[names]}: {round(percent*100, 3)}% ({candidate_votes[names]})")
    f.write('\n'f"--------------------------")
    for highest in range(len(candidate_votes)):
        if mostest < candidate_votes[highest]:
            mostest = candidate_votes[highest]

    hold = candidate_votes.index(mostest)
    winner = candidates[hold]

    f.write('\n'f"Winner: {winner}")
    f.write('\n'f"--------------------------")
        

