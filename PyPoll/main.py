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
        #List of all candidates with votes
        All_Candidates.Append(row[2])
        #Percentage of votes each candidate won
        if Candidate_Totals.get(row[2]):
            Candidate_Totals[row[2]] +=1
        else:
            Candidate_Totals[row[2]] = 0
        #Total number of votes each candidate won

        #Winner of election based on pop vote

















print(f'Election Results')
print(f'----------------')
print(f'Total Votes: {Votes}')
print(f'----------------')







outpath = os.path.join('Analysis', 'Analysis.Txt')
with open (outpath, "w") as textfile:
    textfile.write("Election Results\n")