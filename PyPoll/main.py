import os
import csv

khanVote = 0
correyVote = 0
liVote = 0
otooleyVote = 0
khanVotePer = 0
correyVotePer = 0
liVotePer = 0
otooleyVotePer = 0
winner = ""

#open csv file
csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #calculate total number of votes, and number of votes per candidate
    cnt=0
    for row in csvreader:
        cnt +=1
        if row[2] == "Khan":
            khanVote = khanVote + 1
        elif row[2] == "Correy":
            correyVote = correyVote + 1
        elif row[2] == "Li":
            liVote = liVote + 1
        elif row[2] == "O'Tooley":
            otooleyVote = otooleyVote + 1
    
    #determine election winner
    if khanVote > correyVote and khanVote > liVote and khanVote > otooleyVote:
        winner = "Khan"
    elif correyVote > khanVote and correyVote > liVote and correyVote > otooleyVote:
        winner = "Correy"
    elif liVote > khanVote and liVote > correyVote and liVote > otooleyVote:
        winner = "Li"
    else:
        winner = "O'Tooley"

#calculate percentage of popular votes each candidate received
khanVotePer = (khanVote / cnt)
correyVotePer = (correyVote / cnt)
liVotePer = (liVote / cnt)
otooleyVotePer = (otooleyVote / cnt)

khanVotePer = ("{:.3%}".format(khanVotePer))
correyVotePer = ("{:.3%}".format(correyVotePer))
liVotePer = ("{:.3%}".format(liVotePer))
otooleyVotePer = ("{:.3%}".format(otooleyVotePer))


#display election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {cnt}")
print("-------------------------")
print(f"Khan: {khanVotePer} ({khanVote})")
print(f"Correy: {correyVotePer} ({correyVote})")
print(f"Li: {liVotePer} ({liVote})")
print(f"O'Tooley: {otooleyVotePer} ({otooleyVote})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Specify the file to write to
output_path = os.path.join("pypollresults.txt")

# Write results to file
with open(output_path, 'w', newline='') as pypollfile:

    # Initialize csv.writer
    csvwriter = csv.writer(pypollfile)

    # Write the rows
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {cnt}"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Khan: {khanVotePer}% ({khanVote})"])
    csvwriter.writerow([f"Correy: {correyVotePer}% ({correyVote})"])
    csvwriter.writerow([f"Li: {liVotePer}% ({liVote})"])
    csvwriter.writerow([f"O'Tooley: {otooleyVotePer}% ({otooleyVote})"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])
