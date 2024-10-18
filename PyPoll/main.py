import csv
import os
import pandas as pd

#Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
totalVotes = 0
i = 0
original_df = pd.read_csv(file_to_load)
votes = original_df['Candidate'].value_counts(sort=False).tolist()
canidatesList = original_df['Candidate'].unique().tolist()
winningCandidate = ["",0]
totalVotes = sum(votes)

#Store the header row
header = original_df.columns.tolist()

# Generate and print the winning candidate summary
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")

#loops through canidatesList prints the votes and calculating the candidatePercentage to print 
for candidate in canidatesList:
    candidatePercentage = (round((votes[i] / totalVotes) * 100, 3))
    print(candidate + ": " + str(candidatePercentage) + "% (" + str(votes[i]) + ")\n")

    if votes[i] > winningCandidate[1]:
        winningCandidate[0] = candidate
        winningCandidate[1] = votes[i]
        
    i += 1
        
print("-------------------------")
print("Winner: " + winningCandidate[0])
print("-------------------------")

# Open a text file to save the output
i = 0
with open(file_to_output, "w") as textFile:
    textFile.write("Election Results\n")
    textFile.write("----------------------------\n")
    textFile.write("Total Votes: " + str(totalVotes) + "\n")
    textFile.write("----------------------------\n")

    #loops through canidatesList prints the votes and calculating the candidatePercentage to write 
    for candidate in canidatesList:
        candidatePercentage = (round((votes[i] / totalVotes) * 100, 3))
        textFile.write(str(candidate) + ": " + str(candidatePercentage) + "% (" + str(votes[i]) + ")\n")
        
        i += 1

    textFile.write("----------------------------\n")
    textFile.write("Winner: " + winningCandidate[0] + "\n")
    textFile.write("----------------------------\n")
