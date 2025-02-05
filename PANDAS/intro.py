import numpy as np
import pandas as pd

dict = {
    "name":["abhi","dev","jhala","vikash"],
    "marks":["55","65","76","50"],
    "city":["noida","delhi","bhuj","gurgaon"]
}

df=pd.DataFrame(dict)
# df = df[["name","marks","city"]] #to reverse the columns 
print(df)

# df.to_csv('friends.csv')
# df.to_csv('friends_index.csv', index=False) # this will no provide the index
print(df.head(2))

print(df.tail(2))

print(df.describe())

abhi=(pd.read_csv("abhi.csv"))
print(abhi)
print(abhi["speed"])

#make changes to the csv file
abhi["speed"][0]=50
print(abhi.to_csv("abhi.csv"))
