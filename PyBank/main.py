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
    Greatest_Increase = 0
    Greatest_Decrease = 0
    Greatest_Month_Increase = ""
    Greatest_Month_Decrease = ""

    for row in csvreader:
        Months += 1
        Total_Value += int(row[1])
        

        if not First_Time:
            Change=int(row[1]) - Previous
            Total_Change = Total_Change + Change
            if Change > Greatest_Increase:
                Greatest_Increase = Change
                Greatest_Month_Increase = row[0]
            if Change < Greatest_Decrease:
                Greatest_Decrease = Change
                Greatest_Month_Decrease = row[0]
       
        Previous = int(row[1])
        First_Time = False
        
    
print("Financial Analysis")
print("------------------")   
print(f"Total months: {Months}")
print(f"Total: {Total_Value}")
print(f"Total Change: {Total_Change/(Months-1)}")
print(Greatest_Month_Increase, Greatest_Increase)
print(Greatest_Month_Decrease, Greatest_Decrease)

