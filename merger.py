import csv

import pandas as pd

df1 = pd.read_csv('brown_planet_data.csv')
df2 = pd.read_csv('stars_data.csv')

headers = ['Star_name','Distance','Mass','Radius']

df1_clean = pd.DataFrame()
df2_clean = pd.DataFrame()

for header in headers:
    df1_clean[header] = df1[header]
    df2_clean[header] = df2[header]

df1_clean = df1_clean.dropna()
df2_clean = df2_clean.dropna()

print(df1_clean.head())
print(df2_clean.head())

result = pd.concat([df1_clean, df2_clean])

result.to_csv('final.csv', index=False)
