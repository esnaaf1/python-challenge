# PyBank main.py
import os
import csv

budget_data_csv = os.path.join("..","budget_data.csv")

totalProfits = 0
totalMonths = 0

# create placeholder lists 

months = []
profit_values = []
m_changes = []
m_name = []

r_index = 0

# Version 1
# with open(budget_data_csv, newline="") as csvfile:
#     csvreader=csv.reader(csvfile,delimiter=",")
#     csv_header = next(csvfile)


#     # loop through the rows and add them to the lists
#     for row in csvreader:
#         months.append(row[0])
#         profit_values.append(int(row[1]))
# bankRows = zip(months, profit_values)

# # for row in bankRows :
# #     print(f"month {row[0]} profit value {row[1]}")

# for row in bankRows:
#     totalProfits = totalProfits + row[1]
#     totalMonths += 1
    
#     if totalMonths == 1:
#         last_total = row[1]
#     elif totalMonths >1:
#         m_change = row[1] - last_total
#         m_changes.append(m_change)
#         m_name.append(row[0])
#         last_total = row[1]

# changes = zip(m_name, m_changes)

# for row in changes:
#     print(f"Month {row[0]}  Change {row[1]}")

# print(f"Total Months: { totalMonths} ")
# print(f"Total: ${totalProfits}")


#version 2
with open(budget_data_csv, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)

    # loop through the rows and add them to the lists
    for row in csvreader:

        # add the month to monnths list
        months.append(row[0])
        
        # add the profit/loss values tot he profit_values list

        profit_values.append(int(row[1]))
        
        r_index +=1
        
        # if the row index == 1 set the last_value and set the change from last monmth to zero
        if r_index ==1:
            last_value = int(row[1])
            m_changes.append(0)
        # else if r_index greater than 1 calcuate the change from last month
        elif r_index >1:
            m_change = int(row[1]) - last_value
            m_changes.append(str(m_change))
            last_value= int(row[1])

# zip all the current lists into a new list             
monthly_profit_list = zip(months, profit_values, m_changes)

# initialize the sum_of_changes and greatest increase and descrease variables
sum_of_changes = 0.0
g_increase_value = 0
g_increase_month = ""

g_decrease_value = 0
g_decrease_month = ""

for row in monthly_profit_list:
    totalProfits = totalProfits + row[1]
    sum_of_changes = sum_of_changes + int(row[2])
    totalMonths +=1

    if g_increase_value < int(row[2]):
        g_increase_value = int(row[2])
        g_increase_month = row[0]
    if g_decrease_value > int( row[2]):
        g_decrease_value = int(row[2])
        g_decrease_month = row[0]

   # print(f"Month {row[0]} Profit {row[1]} Change since last month {row[2]}")


#print the finanacial analysis

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {totalMonths} ")
print(f"Total: ${totalProfits}")
print(f"Average change ${round(float(sum_of_changes/(totalMonths-1)),2)}")
print(f"Greatest increase in profits: {g_increase_month} (${g_increase_value})")
print(f"Greatest decrease in profits: {g_decrease_month} (${g_decrease_value})")

