## Dates and strings in Python ##

# Datetimes #
import pandas as pd
time1 = pd.Series('1954-04-30 05:00:00')
time1
time2 = time1.astype('datetime64')
time2
time2.astype('str')
time3 = time2.astype('int64')
time3
time3.astype('datetime64')
num_days = pd.Series(10**4)
num_days.astype('datetime64[D]')
num_secs = pd.Series(10**9)
num_secs.astype('datetime64[s]')
time2.apply(lambda x: x.weekday)

# String length #
import numpy as np
presidents = pd.Series(['Donald Trump', 'Bill Clinton',
    '', np.nan])
presidents
presidents.str.len()

# Extract substrings #
'2016-10-06'[0:4]
dates = pd.Series(['2016-10-06', '2015-08-19', '2016-01-30'])
dates.str[0:4]

# Paste multiple strings into a single string #
'Leo' + 'nard'
firstnames = pd.Series(['Marvin', 'Leonard'])
secondnames = pd.Series(['Gaye', 'Cohen'])
firstnames + ' ' + secondnames

# Conversion to lowercase #
students = pd.Series(['Pablo', 'Liudmila', 'Nana Yaa'])
students.str.lower()

# Detect the presence of a pattern in a string #
students.str.contains('an')

# Extract matching patterns from a string #
students.str.findall('a')

# Replace matched patterns in a string #
students.str.replace(' ', '-')
students.str.replace('o| ', '-')

# Splitting up a string into pieces #
sayings = pd.Series(['Correlation is not causation',
    'Flattery is the food of fools'])
sayings.str.split(' ')

# Regular expressions #
bio = pd.Series(['I was born in 1954',
    'My phone is +34 932 534 200'])
bio.str.replace('[a-z]', 'x')
bio.str.replace('[0-9]', 'x')
bio.str.replace('[a-zA-Z]+', 'x')
bio.str.replace('[0-9]{1,3}', 'x')
bio.str.findall('[a-zA-Z0-9]+')
