import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')


with open(election_data, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    Votes = 0
    All_Candidates = []
    Candidate_Totals = {}

    for row in csvreader:
        Votes += 1
        All_Candidates.append(row[2])
        if Candidate_Totals.get(row[2]):
            Candidate_Totals[row[2]] +=1
        else:
            Candidate_Totals[row[2]] = 1
        #Percentage each candidate won
        #Total number of votes each candidate won
        #Winner of election based on pop vote


print(f'Election Results')
print(f'----------------')
print(f'Total Votes: {Votes}')
print(f'----------------')
for votes in Candidate_Totals.items():
    print(votes)




outpath = os.path.join('Analysis', 'Analysis.Txt')
with open (outpath, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write(f'----------------')
    textfile.write(f'Total Votes: {Votes}')
    textfile.write(f'----------------')  