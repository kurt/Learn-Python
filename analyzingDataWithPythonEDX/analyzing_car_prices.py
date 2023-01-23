import pandas as pd
import numpy as np

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)
df = pd.read_csv(URL, header = None)
df.columns = headers
df1=df.replace('?', np.NaN)
df=df1.dropna(subset=["price"], axis=0)
print(df.head(1))
# prints the datatypes of the data
df.dtypes
# default statistics
print(df.describe())
print(df.describe(include="all"))
print('hello')

first_two_columns = [['column 1', 'column 2'] ]
#save to a file
df.to_csv("automobile.csv", index=False)
#print info including datatypes
print(df.info())
