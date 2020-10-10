import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')


with open(budget_data, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    Months = 0
    Total_Value = 0 
    Previous = 0
    Total_Change = 0
    First_Time = True

    for row in csvreader:
        Months += 1
        Total_Value += int(row[1])
        

        if not First_Time:
            Change=int(row[1]) - Previous
            Total_Change = Total_Change + Change
       
        Previous = int(row[1])
        First_Time = False
        
    
print("Financial Analysis")
print("------------------")   
print(Months)
print(Total_Value)
print(Total_Change/(Months-1))


