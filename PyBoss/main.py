import os
import csv
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)

csvpath = os.path.join('Resources','employee_data.csv')

id = []
name = []
first_name = []
last_name = []
date = []
new_date_list = []
ssn = []
ssn_last = []
state = []
new_state_list = []


with open(csvpath, "r", encoding="utf8") as csvFile:
    csvreader = csv.reader(csvFile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        id.append(row[0])
        name.append(row[1])
        date.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

#name split
    for element in name:
        parts = element.split(' ')
        first_name.append(parts [0])
        last_name.append(parts [1])


#ssn mask
    for element in ssn:
        ssn_parts=element.split("-")
        ssn_last.append("***-**-"+ ssn_parts[2])


#date conversion
    for i in date:
        new_date = datetime.datetime.strptime(i, '%Y-%m-%d')
        new_date_list.append(new_date.strftime('%m/%d/%Y'))

    
#state conversion
    for i in state:
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
            'Wyoming': 'WY'}
        
        new_state = us_state_abbrev[i]
        new_state_list.append(new_state)
    

cleaned_csv = zip(id, first_name, last_name, new_date_list, ssn_last, new_state_list)

output_file = os.path.join("Analysis","new_employee_data.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile, delimiter=',')

    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])

    writer.writerows(cleaned_csv)