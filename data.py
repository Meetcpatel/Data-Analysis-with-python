# Import pandas library
import pandas as pd

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header = None)

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe\n") 

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

#print("headers\n", headers)

df.columns=headers

pricedrop = df.dropna(subset=["price"], axis=0)

topfive = df.head(100)

print(topfive)

df.to_csv("automobile.csv", index=False)

