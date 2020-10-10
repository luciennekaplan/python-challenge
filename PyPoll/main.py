import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')


with open(election_data, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)




























outpath = os.path.join('Analysis', 'Analysis.Txt')
with open (outpath, "w") as textfile:
    textfile.write("Election Results\n")