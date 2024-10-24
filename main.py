import csv
import os

#Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Define variables to track the financial data
totalVotes = 0
i = 0

# Define lists and dictionaries to track candidate names and vote counts
candidateNameList = []
candidateVoteList = []

# Winning Candidate and Winning Count Tracker
winningCandidate = [" ", 0]

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        #Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        totalVotes += 1

        # Get the candidate's name from the row
        # If the candidate is not already in the candidate list, add them
        if row[2] not in candidateNameList:
            candidateNameList.append(row[2])
            candidateVoteList.append(1)

        else:
            # Add a vote to the candidate's count
            candidateVoteList[candidateNameList.index(row[2])] += 1


# Generate and print the winning candidate summary
print("\nElection Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")

#loops through canidatesList prints the votes and calculating the candidatePercentage to print 
for candidate in candidateNameList:
    candidatePercentage = (round((candidateVoteList[i] / totalVotes) * 100, 3))
    print(candidate + ": " + str(candidatePercentage) + "% (" + str(candidateVoteList[i]) + ")\n")

    if candidateVoteList[i] > winningCandidate[1]:
        winningCandidate[0] = candidate
        winningCandidate[1] = candidateVoteList[i]
        
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
    for candidate in candidateNameList:
        candidatePercentage = (round((candidateVoteList[i] / totalVotes) * 100, 3))
        textFile.write(str(candidate) + ": " + str(candidatePercentage) + "% (" + str(candidateVoteList[i]) + ")\n")
        
        i += 1

    textFile.write("----------------------------\n")
    textFile.write("Winner: " + winningCandidate[0] + "\n")
    textFile.write("----------------------------\n")
