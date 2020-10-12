import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')


with open(election_data, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    Total_Votes = 0
    All_Candidates = []
    Candidate_Totals = {}
    Votes = 0
    Totals = 0
    Winning_Votes = 0

    for row in csvreader:
        Total_Votes += 1
        All_Candidates.append(row[2])
        if Candidate_Totals.get(row[2]):
            Candidate_Totals[row[2]] +=1
        else:
            Candidate_Totals[row[2]] = 1
        

print(f'Election Results')
print(f'----------------')
print(f'Total Votes: {Total_Votes}')
print(f'----------------')
for candidates in Candidate_Totals:
   Votes = (Candidate_Totals[candidates])
   Totals = Votes/Total_Votes * 100
   if Candidate_Totals[candidates] > Winning_Votes:
       Winning_Votes = Candidate_Totals[candidates]
       Winning_Candidate = candidates
   print(f'{candidates} : {round(Totals, 3)}% , {Candidate_Totals[candidates]} ')
print(f'----------------')
print(f'Winner: {Winning_Candidate}')  
print(f'----------------')




outpath = os.path.join('Analysis', 'Analysis.Txt')
with open (outpath, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write(f'----------------\n')
    textfile.write(f'Total Votes: {Total_Votes}\n')
    textfile.write(f'----------------\n')  
    for candidates in Candidate_Totals:
        Votes = (Candidate_Totals[candidates])
        Totals = Votes/Total_Votes * 100
        textfile.write(f'{candidates} : {round(Totals, 3)}% , {Candidate_Totals[candidates]}\n')
        if Candidate_Totals[candidates] > Winning_Votes:
            Winning_Votes = Candidate_Totals[candidates]
            Winning_Candidate = candidates
    textfile.write(f'----------------\n')
    textfile.write(f'Winner: {Winning_Candidate}\n')