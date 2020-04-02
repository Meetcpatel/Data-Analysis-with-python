import pandas as pd

df = pd.read_csv('original.csv', sep=',', header=0)
#print(df)
#sum_of_bytes = sum(df)
# df = df.groupby('url')['bytes'].sum() 
#print(df)
#print(sum_of_bytes)
def male_bytes(row):
    if row['gender'] == 'Male':
        return row['bytes']

df['male_bytes'] = df.apply(male_bytes, axis=1)
# print(df)
def female_bytes(row):
    if row['gender'] == 'Female':
        return row['bytes']

df['Female_bytes'] = df.apply(female_bytes, axis=1)

df = df.groupby('url')['Female_bytes','male_bytes'].sum()
print(df)