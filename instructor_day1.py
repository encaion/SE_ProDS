1 + 1
print("sds")

#%%
"a" + "b" + "c"
"aa" * 3

t1 = "abc"
t2 = "def"
t1 + t2

#%%
print("\a")

#%%
tx = "Hello!"
tx[0]
tx[3]
tx[0:4]
tx[-1]
tx[-2]
tx[2:]
tx[:2]

tx[-2:]

#%%
[1, 2, 3]
[1, 2, ["a", "b", "c"]]

aa = [1, 2, 3]
type(aa)
type("aad")
type(1)
type(1.1)

#%%
aa = [1, 2, 3]
bb = [4, 5, 6]
aa + bb
aa * 2

aa[0]
aa[0:1]
aa[1:]

bb = [1, 2, ["a", "b", "c"]]
bb[1]
bb[2]
bb[2][0]

#%%
aa = [1, 2, 3]
aa[0] = 55
print(aa)

bb = [2, 3, 4]
bb[2] = [99, 99]
bb

cc = [3, 4, 5]
cc[1:2] = [99, 99]
cc

dd = [4, 5, 6]
dd[2:2] = [99, 99]
dd

#%%
kk = [1, 2, 3]
del kk[0]
kk

kk = [1, 2, 3]
del kk[0:2]
kk

gg = [1, 2, 3]
gg.extend(["a", "b"])
gg

gg = [1, 2, 3]
gg.append(["a", "b"])
gg

#%%
ww = [2, 5, 3]
ww.sort()
ww

#%%
mm = [1, 2, 3]
mm.index(1)
mm.index(3)
mm.index(5)

ff = [1, 2, 2, 3, 5, 5]
ff.index(2)

2 in mm
mm.count(2)
ff.count(2)
set(ff)
len(ff)

#%%
ss = [1, 2, 3]
ss.insert(2, 99)
ss

#ss = [1, 2, 3]
#ss[2:2] = [99]
#ss

ss = [1, 2, 3]
ss.insert(5, 99)
ss

tt = [1, 2, 3, 2]
tt.remove(2)
tt

#%%
(1, 2, 3)
(1, 2, (5, 6, 7))
aa = (1, 2, [5, 6, 7])
aa
aa[2]
aa[2][0]

tp1 = (1)
type(tp1)

tp2 = (1,)
type(tp2)

aa
aa[2]    
type(aa[2])
aa[2] = 3
aa[2][0] = 3
aa

#%%
import numpy as np
np.average([1, 2, 3])

#%%
np.array([1, 2, 3])
np.array([[1, 2], [3, 4]])

#%%
data = np.array([2, 4, 7, 9.1])
data.ndim
data.shape
data.dtype

data.reshape(2, 2)

#%%
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr

arr[0]
arr[0][0]

arr[0, 1:]
arr[0, 1:2]

#%%
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr

arr_sub = arr[0, 0:2]
arr_sub

arr[0, 0:2] = [99, 88]
arr
arr_sub

arr_sub = arr[0, 0:2].copy()
arr_sub

arr[0, 0:2] = [3, 4]
arr
arr_sub

#%%
import pandas as pd
pd.Series([2, 4, 6, 8])

ser = pd.Series([2, 4, 6, 8])
ser.values
ser.index

#%%
ser2 = pd.Series([2, 4, 6, 8], index = ["a", "b", "c", "d"])
ser2[1]
ser2[1] = 1
ser2[1] = "asdf"
ser2["b"] = "asdf"
ser2
ser2.dtype

#%%
values = {"aa": [1, 2, 3],
          "bb": ["a", "b", "c"]}
df = pd.DataFrame(values)

df = pd.DataFrame({"aa": [1, 2, 3],
                   "bb": ["a", "b", "c"]})
df.index
df.values

#%%
df.aa
df["aa"]
df["aa"][1]
df["aa"][:2]

df.columns
df.columns[1]
df.columns = ["xx", "yy"]
df.columns

#df.columns[1] = "cc"

# 1)
df = df.rename(columns = {"xx": "obs"})
# 2)
df.rename(columns = {"xx": "obs"}, inplace = True)
df.columns

df[["obs", "yy"]]
df[["yy", "obs"]]

#%%
import pandas as pd
df = pd.read_excel("iris_xlsx.xlsx")
df.head()
df.to_csv("write_csv_test.csv")

df = pd.read_csv("bike.csv")
df.to_json(r"bike.json", orient = "records")

df = pd.read_json("bike.json")
df.head()

#%%
#### 5. 데이터 처리 기술 ####

#%%
import numpy as np
import pandas as pd
df = pd.read_csv("bike.csv")
df.head()

df.head(2)
df.tail(3)

df.columns
df.shape
df.size
df.dtypes

df.shape[0]
df.shape[1]

df.ix[1]

df.iloc[0, 0]

df.iloc[0, :2]
df_sub = df.iloc[0, :2]
type(df_sub)

#%%
import numpy as np
nums = [1, 2, 2, 5, 8, 8]
len(nums)
dd = set(nums)
type(dd)

len(set(nums))

np.unique(nums)
set(nums)

np.mean(nums)
np.average(nums)
