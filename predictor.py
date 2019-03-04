import numpy as np
import pandas as pd

# Define common header

#Variables
income_h = 'IRFAMIN3'
gender_h = 'IRSEX'
race_h = 'NEWRACE2'
grade_h = 'EDUSCHGRD2'

# category values (CHANGE TO YOUR NEEDS)
selincome = 3 # $20,000 - $29,999
selgender = 1 # Male
selrace = 1 # Nonhispanic, White
selgrade = 8 # Senior
seldrugusage_h = 'CIGEVER'

print('starting load, may take some time')
df = pd.read_csv('NSDUH_2017_Tab.tsv', sep='\t', low_memory=False)
print('finished loading')


# The number of people whom'st'd've are in the group 

# count the number of people in this category
total = 0
# the number of people in this category who use said drug
users = 0

for row in df[[income_h, gender_h, race_h, grade_h, seldrugusage_h]].iterrows():
    # If the row meets our requirements
    if row[1][income_h] == selincome and row[1][gender_h] == selgender and row[1][race_h] == selrace and row[1][grade_h] == selgrade:
        total += 1
        # If the person has used it in the past year
        if row[1][seldrugusage_h] < 3:
            users += 1

# print prob value to screen
print('your chance of having used this drug is: ' + users/total)
