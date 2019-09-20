
# PayBank main.py
# Farshad Esnaashari M/W session
# Submitted by Farshad Esnaashari

# import packages
import os
import csv

# Set the path for the csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# initialize the variables to capture the totals
total_profits = 0
total_months = 0

# initialize the variables ot capture the changes
monthly_change = 0
sum_of_changes = 0

# initialize the variables to capture the greatest increases
greatest_inc = 0
greatest_inc_month = ""

# initialize the variables to capture the greatest descreases
greatest_dec = 0
greatest_dec_month = ""

# open the budget_data.csv

with open(budget_data_csv, newline="") as csvfile:
    
    # read the rows into the csvreader
    csvreader=csv.reader(csvfile,delimiter=",")

    # read the header
    csv_header = next(csvfile)

    # loop through the rows in the file
    for row in csvreader:

        # increment the total months
        total_months +=1

        # add to the total_profits
        total_profits = total_profits+ int(row[1])
        
        # if the total_months == 1 then set the last_value to the current profit
        if total_months ==1:
            last_value = int(row[1])
        # else if total_months > 1 calcuate the monthly_change, and set the last value to the current profit
        elif total_months >1:
            monthly_change = int(row[1]) - last_value
            last_value= int(row[1])

        # calculate sum_of_changes
        sum_of_changes = sum_of_changes + monthly_change

        # update the the greatest increase
        if greatest_inc < monthly_change:
            greatest_inc = monthly_change
            greatest_inc_month = row[0]

        # update the greatest decrease
        if greatest_dec > monthly_change:
            greatest_dec = monthly_change
            greatest_dec_month = row[0]

#print the finanacial analysis to the terminal

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_months} ")
print(f"Total: ${total_profits}")
print(f"Average change ${round(float(sum_of_changes/(total_months-1)),2)}")
print(f"Greatest increase in profits: {greatest_inc_month} (${greatest_inc})")
print(f"Greatest decrease in profits: {greatest_dec_month} (${greatest_dec})")

# set the path for the text file
output_path= os.path.join("Outputs", "PyBank_output.txt")

# open the text file
with open (output_path, 'w', newline='') as txtfile:

    # write the results to the text file
    txtwriter = txtfile.write("Financial Analysis\n")
    txtwriter = txtfile.write("-----------------------------\n")
    txtwriter = txtfile.write(f"Total Months: {total_months}\n")
    txtwriter = txtfile.write(f"Total: ${total_profits}\n")
    txtwriter = txtfile.write(f"Average change ${round(float(sum_of_changes/(total_months-1)),2)}\n")
    txtwriter = txtfile.write(f"Greatest increase in profits: {greatest_inc_month} (${greatest_inc})\n")
    txtwriter = txtfile.write(f"Greatest decrease in profits: {greatest_dec_month} (${greatest_dec})\n")
