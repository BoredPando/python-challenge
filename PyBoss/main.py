# Import Dependencies 
import csv
import pandas as pd

# Input file path 
csv_file_path = ("employee_data.csv")

# Declare Variables
full_name = []
first_name = []
last_name = []
date_of_birth = []
d_o_b = []
ssn = []
ssn_private = []
abbrev = []
employee_id = []


# Dictionary containing state abbrev
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

# Open CSV
with open(csv_file_path,newline="") as employee_data:
    csvreader = csv.reader(employee_data,delimiter=",") 

    # Skip the header 
    header = next(csvreader)     
    
    # Iterate through each row
    for row in csvreader:

        # Append employee id's into list
        employee_id.append(row[0])


        # Split full name into first name and last name lists 
        full_name = row[1].split(" ")   
        first_name.append(full_name[0])
        last_name.append(full_name[1])

        # Split date of birth by "-"
        # Append and format date of birth into d_o_b list
        date_of_birth = row[2].split("-")
        d_o_b.append(date_of_birth[1] + "/" + date_of_birth[2] + "/" + date_of_birth[0])
        

        # Split the SSN by "-"
        # Append and format ssn into ssn_private list 
        ssn = row[3].split("-")
        ssn_private.append("***-**-" + ssn[2])

        # Match the state list item to a dictionary value, if they match, append dictionary key to list abbrev
        abbrev.append(us_state_abbrev[row[4]])

# Use pandas library to create Data Frame Object 
# Keys replace orignal headers, values are the lists created 
new_df = pd.DataFrame({"Employee Id": employee_id, "First Name": first_name, "Last Name": last_name, "DOB": d_o_b, "SSN":ssn_private, "State": abbrev})

# Export new_df to csv
new_df.to_csv(("employee_data_reformatted.csv"), index=False, header=True)

# Print sample data 
print(new_df.head())