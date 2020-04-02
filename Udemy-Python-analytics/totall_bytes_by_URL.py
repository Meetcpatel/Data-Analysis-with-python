import pandas as pd

df = pd.read_csv('original.csv', sep=',', header=0)
#print(df)
#sum_of_bytes = sum(df)
# def int_bytes(row):
#     inbytes = row['bytes']
#     bytes_int = float(inbytes)
#     return bytes_int
# df['clean_bytes'] = df.apply(int_bytes, axis=1)

df = df.groupby('url')['bytes'].sum() 
print(df)
#print(sum_of_bytes)