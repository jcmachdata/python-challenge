import os
import csv

full_name=[]
name=""
first_names=[]
last_names=[]
birth_dates=[]
new_birth_dates=[]
social=""
date=""
social_num=[]
masked_social=[]
state=""
abbrev_states=[]
ids=[]
new_list=[]
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#open employee data
csvpath = os.path.join('employee_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #split the name, rearrange birthdate, mask social, and abbreviate state
    for row in csvreader:
        ids.append(row[0])
        
        name=row[1]
        full_name = name.split(" ")
        first_names.append(full_name[0])
        last_names.append(full_name[1])
        
        date=row[2]
        birth_dates = date.split("-")
        new_birth_dates.append(f"{birth_dates[1]}/{birth_dates[2]}/{birth_dates[0]}")
        
        social=row[3]
        social_num = social.split("-")
        masked_social.append(f"***-**-{social_num[2]}")
        
        state=row[4]
        abbrev_states.append(us_state_abbrev[state])
    
    #combine results in new list
    new_list=zip(ids,last_names,first_names,new_birth_dates,masked_social,abbrev_states)   
    
# Specify the file to write to
output_path = os.path.join("new_data.csv")
employee_list = list(new_list)

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as employeefile:

    # Initialize csv.writer
    csvwriter = csv.writer(employeefile)

    # Write the rows
    csvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN", "State"])
    for row in employee_list:
        csvwriter.writerow(row)        