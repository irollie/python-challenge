import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
totalMonths = 0
netTotal = 0
lastRowsChange = 0
change = []
greatestIncrease = [" " , 0]
greatestDecrease = [" " , 0]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter = ",")

    #Store the header row
    header = next(reader)
    
    # Process each row of data
    i = 0
    for row in reader:
        # Track the total
        totalMonths += 1
        netTotal += int(row[1])
        
        if i == 0:
            change.append(0)
        else:
            change.append((int(row[1])) - (lastRowsChange))

        # Calculate the greatest increase in profits (month and amount)
        if change[i] > int(greatestIncrease[1]):
            greatestIncrease[0] = (row[0])
            greatestIncrease[1] = (change[i])

        # Calculate the greatest decrease in losses (month and amount)
        if change[i] < int(greatestDecrease[1]):
            greatestDecrease[0] = (row[0])
            greatestDecrease[1] = (change[i])
    
        i += 1
        lastRowsChange = int(row[1])
        
#solve for averageChange and format two decimal places
averageChange = sum(change) / (totalMonths - 1)
averageChange = str(round(averageChange, 2))

# Print the output
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalMonths))
print("Total: $" + str(netTotal))
print("Average Change: $" + str(averageChange))
print("Greatest Increase in Profits: " + greatestIncrease[0] + " ($" + str(greatestIncrease[1]) + ")")
print("Greatest Decrease in Profits: " + greatestDecrease[0] + " ($" + str(greatestDecrease[1]) + ")")

#Output to file
with open(file_to_output, "w") as textFile:
    textFile.write("Financial Analysis\n")
    textFile.write("----------------------------\n")
    textFile.write("Total Months: " + str(totalMonths) + "\n")
    textFile.write("Total: $" + str(netTotal) + "\n")
    textFile.write("Average Change: $" + str(averageChange) + "\n")
    textFile.write("Greatest Increase in Profits: " + greatestIncrease[0] + " ($" + str(greatestIncrease[1]) + ")\n")
    textFile.write("Greatest Decrease in Profits: " + greatestDecrease[0] + " ($" + str(greatestDecrease[1]) + ")\n")
