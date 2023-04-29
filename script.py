import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

#1+2

files = glob.glob("states*.csv")
 
df_list = []

files = glob.glob("states*.csv")
us_census_list = [pd.read_csv(filename) for filename in files]

us_census = pd.concat(us_census_list)

#3+4
#print(us_census.columns)
#print(us_census.dtypes)
#print(us_census.head())

#5
us_census["Income"] = us_census["Income"].str.replace(r"[$]|,", "", regex=True)
us_census["Income"] = pd.to_numeric(us_census["Income"])

#print(us_census.columns)
#print(us_census.dtypes)
print(us_census.head())

#6
us_census["str_split"] = us_census["GenderPop"].str.split("_")
us_census["Men"] = us_census.str_split.str.get(0)
us_census["Women"] = us_census.str_split.str.get(1)
print(us_census.head())

#7
us_census["Men"] = us_census["Men"].replace('[M]', '', regex=True)
us_census["Women"] = us_census["Women"].replace('[F]', '', regex=True)
us_census["Men"] = pd.to_numeric(us_census["Men"])
us_census["Women"] = pd.to_numeric(us_census["Women"])
print(us_census.head())
#print(us_census.dtypes)

#8
plt.scatter(us_census["Women"],us_census["Income"])
plt.show()
plt.clf()

#9
#print(us_census["Women"])
difference = us_census["TotalPop"]-us_census["Men"]
us_census = us_census.fillna(value={"Women":difference})
#print(us_census["Women"])
print(us_census.head())

#10 + 11
#print(us_census.duplicated())
#us_census = us_census.drop(columns = ["Unnamed: 0"])
#us_census = us_census.drop_duplicates().reset_index(drop = True)

#12
plt.scatter(us_census.Women, us_census.Income)
plt.title("The Income of Women")
plt.xlabel("Population of Women")
plt.ylabel("Income")
plt.show()
plt.clf()

#12+13

print(us_census.columns)

ethnics = ["Hispanic","White","Black","Native","Asian","Pacific"]

ethnics = us_census[ethnics]
for column in ethnics.columns:
  ethnics[column] = pd.to_numeric(ethnics[column].str[:-1])
print(ethnics.head())

ethnics = ethnics.fillna(value={"Pacific":100-ethnics.Hispanic -ethnics.White -ethnics.Black-ethnics.Native-ethnics.Asian})
print(ethnics.head())

plt.figure(figsize = [15, 15])
for index, ethnic in enumerate(ethnics.columns):
  ax = plt.subplot(3, 2, index + 1)
  plt.hist(ethnics[ethnic])
  plt.title(ethnic)

plt.suptitle("Ethnics", fontsize = 20)
plt.tight_layout(
  pad = 5
)
plt.show()
plt.clf()

