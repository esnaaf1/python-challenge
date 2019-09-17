# PyBank main.py
import os
import csv

# set the path
budget_data_csv = os.path.join("..","budget_data.csv")

# initialize the variables

total_profits = 0
total_months = 0
monthly_change = 0
total_monthly_changes = 0
g_increase_value = 0
g_increase_month = ""

g_decrease_value = 0
g_decrease_month = ""

# open the budget_data.csv

with open(budget_data_csv, newline="") as csvfile:
    
    # read the rows
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)

    # loop through the rows and add them to the lists
    for row in csvreader:

        # increment the total months

        # add to the total_profits
        
        # if the total_months == 1 save the profit to the last_value
        
        # else if total_months > 1 calcuate the change from last value, and set the last_value to the current month value 
        # add to the total monthly changes
        
        # if the g_increase_value is less than the current value set it the current month value

       # if the g_decrease_value is greater than the current value set it the current month value
        

       
        
#print the finanacial analysis

# print("Financial Analysis")
# print("--------------------")
# print(f"Total Months: {total_months} ")
# print(f"Total: ${total_profits}")
# print(f"Average change ${round(float(total_monthly_changes/(total_months-1)),2)}")
# print(f"Greatest increase in profits: {g_increase_month} (${g_increase_value})")
# print(f"Greatest decrease in profits: {g_decrease_month} (${g_decrease_value})")

#write it to a text file
#output_path= os.path.join("..","PyBank_output.txt")

# open the file
# with open (output_path, 'w', newline='') as txtfile:
#     # write rows
#     txtwriter = txtfile.write("Financial Analysis\n")
#     txtwriter = txtfile.write("--------------------\n")
#     txtwriter = txtfile.write(f"Total Months: {totalMonths}\n")
#     txtwriter = txtfile.write(f"Total: ${totalProfits}\n")
#     txtwriter = txtfile.write(f"Average change ${round(float(sum_of_changes/(totalMonths-1)),2)}\n")
#     txtwriter = txtfile.write(f"Greatest increase in profits: {g_increase_month} (${g_increase_value})\n")
#     txtwriter = txtfile.write(f"Greatest decrease in profits: {g_decrease_month} (${g_decrease_value})\n")