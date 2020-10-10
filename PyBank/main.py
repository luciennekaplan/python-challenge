import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')


with open(budget_data, 'r') as csvfile: 
     csvreader = csv.reader(csvfile, delimiter=',')
     csvheader = next(csvreader)

    Months = 0
    Total_Value = 0 


    for row in csvreader
        Months += 1
        Total_Value = 


