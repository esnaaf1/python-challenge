# PyBank main.py
import os
import csv

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
        total_months +=1

        # add to the total_profits
        total_profits = total_profits+ int(row[1])
        
        # if the total_months == 1 set the last_value and set the change from last monmth to zero
        if total_months ==1:
            last_value = int(row[1])
        # else if total_months > 1 calcuate the change from last month
        elif total_months >1:
            monthly_change = int(row[1]) - last_value
            last_value= int(row[1])
        # add to the total monthly changes
        print(f" month {row[0]}, monthly_change {monthly_change} total_monthly_changes {total_monthly_changes}")
        total_monthly_changes = total_monthly_changes + monthly_change

        # determine the the greatest increase
        if g_increase_value < monthly_change:
            g_increase_value = monthly_change
            g_increase_month = row[0]

        #dtermine the greatest decrease
        if g_decrease_value > monthly_change:
            g_decrease_value = monthly_change
            g_decrease_month = row[0]

#print the finanacial analysis

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months} ")
print(f"Total: ${total_profits}")
print(f"Average change ${round(float(total_monthly_changes/(total_months-1)),2)}")
print(f"Greatest increase in profits: {g_increase_month} (${g_increase_value})")
print(f"Greatest decrease in profits: {g_decrease_month} (${g_decrease_value})")

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


