import  os
import  csv


# Variables needed:
# total number of months included in the dataset
# total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" btw months over the  entire period
#The greatest increase in profits (date and amt) over the entire period
#The greatest decrease in profits (date and amt) over the entire period


#Header: Financial Analysis
#-----------------------------
#Total Months: 86
#Total: $38382578
#Average Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

#path to collect data from Homework folder
pyBankCSV = os.path.join("..", "PyBank", "budget_data.csv")


#Declare variables to track
total_months = 0
total_revenue = 0

#will track the last revenue looped for avg change calc
last_revenue = 867884

#will calculate each revenue change while looping
revnue_change = 0

#track greatest increase/decrease in revenue. Skip first column, track second column
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999999999]

#track total revenue change
revenue_changes = []


# Open the CSV

with open(pyBankCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    #Loop through to calc months/revnue for each row

    for row in csvreader:

        #Calculate the total months
        total_months = total_months +1

        #Caluate total revenue
        total_revenue = total_revenue + int(row[1])

        #Calculate revnue change



        revnue_change = float(row[1]) - last_revenue


        #Update last revnue to last looped row
        last_revenue = int(row[1])

        # Add Revenue changes to revenue change array
        revenue_changes.append(int(revnue_change))

        #Determine greatest increase
        if (revnue_change > greatest_increase[1]):
            greatest_increase[1] = revnue_change

            #record date of greatest change
            greatest_increase[0]= row[0]

        # Determine greatest decrease
        if (revnue_change < greatest_decrease[1]):
            greatest_decrease[1] = revnue_change

            # record date of greatest change
            greatest_decrease[0] = row[0]


    #Calculate avg change: sum of rev changes array / length
    average_change = sum(revenue_changes)/(len(revenue_changes) - 1)
#-------------------------------------------------------------------------
#Display summary of results
summary_results = f""" Financial Analysis
-------------------------------------------------------
Total Months: {total_months}
Total Revenue: ${total_revenue}
Average Change: ${average_change:.2f}
Greatest Increase: {greatest_increase[0]} : ${greatest_increase[1]:.0f}
Greatest Decrease: {greatest_decrease[0]} : ${greatest_decrease[1]: .0f}

"""
#---------------------------------------------------------------------------

print(summary_results)

#---------------------------------------------------------------------------
#open output file and write in results


#Set variable for output file
summary_output_file = os.path.join("financial_analysis.txt")

#Open the output file

with open(summary_output_file, "w", newline="") as textfile:
    writer = textfile.write(summary_results)

#------------------------------------------------------------------------------




