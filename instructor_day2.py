import pandas as pd
df = pd.read_csv("bike.csv")
season = df["season"]

season.value_counts()

df["workingday"].value_counts()

df.iloc[:3, 1:3]
df.iloc[:3, 1:3].sum(axis = 0)
df.iloc[:3, 1:3].sum(axis = 1)

df.iloc[:3, 1:3].mean()
df.iloc[:3, 1:3].mean(axis = 0)
df.iloc[:3, 1:3].mean(axis = 1)

#%%
df["season"].value_counts()
pd.crosstab(df["season"], df["holiday"])

df[["season", "holiday"]].drop_duplicates()
df[["season", "holiday"]].drop_duplicates(keep = "first")
df[["season", "holiday"]].drop_duplicates(keep = "last")

# index 제거 
# 1)
df[["season", "holiday"]].drop_duplicates().reset_index()
df_sub = df[["season", "holiday"]].drop_duplicates().reset_index()
df_sub.columns
df_sub.head()

# 2)
df[["season", "holiday"]].drop_duplicates().reset_index(drop = True)

# groupby
df.iloc[: ,[1, 9]].groupby("season").mean()
df.loc[: ,["season", "casual"]].groupby("season").mean()

df.loc[: ,["season", "workingday", 
           "casual"]].groupby(["workingday", "season"]).mean()
df.loc[: ,["season", "workingday", 
           "casual"]].groupby(["season", "workingday"]).mean()

df.loc[: ,["season", "workingday", 
           "casual", "registered"]].groupby(["workingday", "season"]).mean()

#%%
set(df["season"])
df["season"].unique()

#%%
df_sub = df[df.season == 1]
df_sub.head(2)
df_sub.shape

set(df_sub["season"])
df_sub["season"].unique()

df_sub2 = df[(df.season == 1) & (df.holiday == 1)]
df_sub2.head(2)
df_sub2.shape

set(df_sub2["season"])
set(df_sub2["holiday"])
df_sub2[["season", "holiday"]].drop_duplicates()

df_sub3 = df[(df.season == 1) & (df.season == 2)] # X
df_sub3

df_sub4 = df[(df.season == 1) | (df.season == 2)]
df_sub4
set(df_sub4["season"])

df_sub5 = df[df["season"].isin([1, 3])]
df_sub5
set(df_sub5["season"])

#%%
# 제어문
score = 85
if score >= 80:
    print("A")
    
score = 60
if score >= 80:
    print("A")
else:
    print("F")
    
level = ["A", "B", "C", "D", "E"]
mine = "C"

if mine in level[:1]:
    print("Pass")
elif mine == level[2]:
    print("Retake")
else:
    print("Fail")
    
listt = ["a", "b", "c"]
for i in listt:
    print(i) 
    
a = [(1, 2), 
     (3, 4), 
     (5, 6)]
for (first, last) in a:
    print(first + last)

import numpy as np
for i in np.arange(5):
    print(i)

for _ in np.arange(5):
    print(_)
    
for n in range(10):
    print(n)

# list comprehension
# 1 - for()
vec = []
for n in range(10):
    vec.append(n)
    print(vec)
vec

# 2 - list[]
vec2 = [n for n in range(10)]
vec2

a = [2, 6, 7, 8, 9]
odds = [num for num in a if num % 2 == 0]

odds = []
for num in a:
    if num % 2 == 0:
        odds.append(num)
odds

[num for num in a if num % 2 == 0]


#%%
import pandas as pd
df = pd.read_csv("diamonds.csv")
df.head()

df.loc[:, ["price", "color"]].groupby("color").mean()


