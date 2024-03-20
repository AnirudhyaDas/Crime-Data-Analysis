import pandas as pd


crime_data = pd.read_csv("District_wise_crime.csv", sep=',', encoding="ISO-8859-1")

df = crime_data.rename(columns={'Êstatename':'STATE/UT'})
df = crime_data.replace('?', '0')
df.head()

df.loc[df['YEAR'] == '?']

df.loc[df['MURDER'] == '?']

