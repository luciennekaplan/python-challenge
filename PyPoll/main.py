import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')


with open(election_data, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    Votes = 0

    for row in csvreader:
        election_results = {
        "Voter ID": int(row[0]),
        "County" : str(row[1]),
        "Candidate" : str(row[2])
         }
        Votes += 1
















print(f'Election Results')
print(f'----------------')
print(f'Total Votes: {Votes}')
print(f'----------------')







outpath = os.path.join('Analysis', 'Analysis.Txt')
with open (outpath, "w") as textfile:
    textfile.write("Election Results\n")