## Assignment 1 - Airbnb postings in New York City ##

# Importing data (use the appropriate path) #
import pandas as pd
df = pd.read_csv('airbnb.csv')

# Q1. Date the host started #
cond1 = df['host_since'] < '2010-01-01'
cond1.sum()
df['host_id'][cond1].unique().shape

# Q2. Missing rating #
df['rating'].isna().sum()

# Q3. Price distribution #
import matplotlib.pyplot as plt
df['price'].plot.hist(title='Figure 1. Price histogram', figsize=(6,6), color='0.7')
df['price'][df['price'] < 500].plot.hist(title='Figure 2. Price histogram (trimmed data)', figsize=(6,6), color='0.7')

# Q4. Average price per room type #
pd.pivot_table(data=df, columns='room_type', values='price', aggfunc='mean')
pd.pivot_table(data=df, columns='room_type', values='price', aggfunc='median')

# Q5. Variation across neighbourhoods #
pd.pivot_table(data=df, columns='neighbourhood', index='room_type', values='price', aggfunc='median')

# Q6. Counts per room type and neighbourhood #
pd.pivot_table(data=df, columns='neighbourhood', index='room_type', values='host_id', aggfunc='count')
pd.crosstab(df['neighbourhood'], df['room_type'])

# Dropping rows with missing values #
host_since1 = df['host_since'].dropna()
df1 = df.dropna()

# Dropping duplicates #
df.duplicated().sum()
df = df[df.duplicated() == False]
