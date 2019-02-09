import os
import csv

#set inital values to zero
total = 0
avgchange = 0
maxP = 0
minP = 0
maxSpread = 0
minSpread = 0
maxPcnt = 0
minPcnt = 0
minMonth = ""
maxMonth = ""

#open csv file
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #calculate total number of months and total profits
    cnt = 0
    for row in csvreader:
        cnt += 1
        total=total+int(row[1])
        if row[0]=="Jan-2010":
            beginprofit = row[1]
        elif row[0] == "Feb-2017":
            lastprofit = row[1]
        
        #calculate greatest increase in profits
        if int(row[1]) > int(maxP):
            maxSpread = int(row[1]) - int(maxPcnt)
            maxP = int(row[1])
            maxPcnt = int(row[1])
            maxMonth = row[0]
        else: 
            maxPcnt = int(row[1])
                  
        #calculate greatest decrease in profits
        if int(row[1]) < int(minP):
            minSpread = int(row[1]) - int(minPcnt)
            minP = int(row[1])
            minPcnt = int(row[1])
            minMonth = row[0]
        else:
            minPcnt = int(row[1])

#calculate average change            
avgchange = (int(lastprofit) - int(beginprofit))/85  
avgchange = round(avgchange,2)

#display results
print("Financial Analysis")        
print("----------------------------")
print(f"Total Months: {cnt}")
print(f"Total: ${total}")
print(f"Average  Change: ${avgchange}")
print(f"Greatest Increase in Profits: {maxMonth}: $({maxSpread})")
print(f"Greatest Decrease in Profits: {minMonth}: $({minSpread})")

# Specify the file to write to
output_path = os.path.join("pybankresults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as pybankfile:

    # Initialize csv.writer
    csvwriter = csv.writer(pybankfile)

    # Write the rows
    csvwriter.writerow(["Financial Analysis"])        
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {cnt}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow([f"Average  Change: ${avgchange}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {maxMonth}: $({maxSpread})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {minMonth}: $({minSpread})"])
    