import os
import csv

budget_data = os.path.join('..', 'uofo-por-data-pt-09-2020-u-c', '03-Python', 'HW', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')





with open(budget_data, 'r') as csvfile: 
      csvreader = csv.reader(csvfile, delimiter=',')
