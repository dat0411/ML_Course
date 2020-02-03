## Skills requested in Google job posts ##

# Importing the data #
import pandas as pd
fname = 'https://raw.githubusercontent.com/mcanela-iese/ML_Course/master/Data/' \
    'skills_google.csv'
df = pd.read_csv(fname, encoding='utf-8')
df.info()

# Exploring the company #
df['company'].value_counts()

# Exploring the job titles #
title = df['title']
title.unique().shape
title.value_counts()[:10]
title.str.contains('Intern').sum()
title.str.contains('Sales').sum()
title.str.contains('Cloud').sum()
title.str.contains('Google Cloud').sum()
title = title.str.replace(pat=' [(].+[)]', repl='')
title.str.split(pat=', ').head()
L = list(title.str.split(', '))
L[:5]
title = L[0]
for x in L[1:]:
    title = title + x
title[:5]
len(title)
pd.Series(title).value_counts()[:10]

# Exploring categories #
df['category'].value_counts()[:15]

# Exploring countries #
country = df['location']
country.head()
country = country.str.replace(pat='.+, ', repl='')
country.unique().shape
country.value_counts()[:10]

# Exploring responsibilities #
resp = df['responsibilities']
resp.isna().sum()
resp = resp.dropna()
resp = resp.str.lower()
resp.iloc[0]
L = resp.str.findall('[a-z]+')
L[:5]
resp = L[0]
for x in L[1:]:
    resp = resp + x
resp[:5]
len(resp)
pd.Series(resp).value_counts()[:25]

# Exploring minimum qualifications #
minqual = df['minqual']
minqual.isna().sum()
minqual = minqual.dropna()
minqual = minqual.str.lower()
minqual.iloc[0]
L = minqual.str.findall('[a-z]+')
L[:5]
minqual = L[0]
for x in L[1:]:
    minqual = minqual + x
minqual[:5]
pd.Series(minqual).value_counts()[:25]
pd.Series(minqual).str.contains('sql').sum()
pd.Series(minqual).str.contains('javascript').sum()
pd.Series(minqual).str.contains('python').sum()

# Exploring preferred qualifications #
prefqual = df['prefqual']
prefqual.isna().sum()
prefqual = prefqual.dropna()
prefqual = prefqual.str.lower()
prefqual.iloc[0]
prefqual = L[0]
for x in L[1:]:
    prefqual = prefqual + x
prefqual[:5]
len(prefqual)
pd.Series(prefqual).value_counts()[:25]
pd.Series(prefqual).str.contains('sql').sum()
pd.Series(prefqual).str.contains('javascript').sum()
pd.Series(prefqual).str.contains('python').sum()
