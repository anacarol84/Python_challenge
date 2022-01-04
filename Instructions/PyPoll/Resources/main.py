# Import libraries
# The OS which stands for operatins systems will allow us to create file paths 
import os
import csv

csvpath = os.path.join('election_data.csv')
print("Election Results")
print("__________________")

#create poll variables
votes = []
candidates = []

# Method 2: Read file using CSV module

with open(csvpath, newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ',')
   print(csvreader)
   csv_header = next(csvreader)
   print(f"CSV Header: {csv_header}")

   for column in csvreader:
       votes.append(column[0])
       candidates.append(column[2])

   Total_Votes = (len(votes))
   print(f"Total Votes: {Total_Votes}")
   #Count number of each candidates in the candidates poll
   Khan = int(candidates.count("Khan"))
   Correy = int(candidates.count("Correy"))
   Li = int(candidates.count("Li"))
   O_Tooley = int(candidates.count("O'Tooley"))

   #Find the porcentage of each candidates vote total
   Khan_percentage = (Khan/Total_Votes) * 100
   Correy_percentage = (Correy/Total_Votes) * 100
   Li_percentage = (Li/Total_Votes) * 100
   O_Tooley_percentage = (O_Tooley/Total_Votes) * 100
   #Print each candidate's name, vote percentage, and raw number of votes
   print(f"Khan: {round(Khan_percentage, 4)}% ({Khan})")
   print(f"Correy: {round(Correy_percentage, 4)}% ({Correy})")
   print(f"Li: {round(Li_percentage, 4)}% ({Li})")
   print(f"O'Tooley: {round(O_Tooley_percentage, 4)}% ({O_Tooley})")
    #Compare Votes and pick winner with the most votes
   if Khan > Correy > Li > O_Tooley:
       Winner = "Khan"
   elif Correy > Khan > Li > O_Tooley:
       Winner = "Correy"
   elif Li > Khan > Correy > O_Tooley:
       Winner = "Li"
   elif O_Tooley > Khan > Correy > Li:
       Winner = "O'Tooley"
   print(f"Winner: {Winner}")
   
# second option of output file   
# output_path = os.path.join("election.txt")
# with open(output_path, 'w', newline='') as txtfile:
#     txtfile.write(f"Total Votes: {Total_Votes}")
#     txtfile.write(f"Khan: {round(Khan_percentage, 4)}% ({Khan})")
#     txtfile.write(f"Correy: {round(Correy_percentage, 4)}% ({Correy})")
#     txtfile.write(f"Li: {round(Li_percentage, 4)}% ({Li})")
#     txtfile.write(f"O'Tooley: {round(O_Tooley_percentage, 4)}% ({O_Tooley})")
#     txtfile.write(f"Winner: {Winner}")
#     txtfile.close()

# exporting a text file with the results
election_file = os.path.join("election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {Total_Votes}")
    outfile.write("-------------------------\n")
    outfile.write(f"Khan: {round(Khan_percentage, 4)}% ({Khan})")
    outfile.write(f"Correy: {round(Correy_percentage, 4)}% ({Correy})")
    outfile.write(f"Li: {round(Li_percentage, 4)}% ({Li})")
    outfile.write(f"O'Tooley: {round(O_Tooley_percentage, 4)}% ({O_Tooley})")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {Winner}")
    outfile.write("-------------------------\n")    


