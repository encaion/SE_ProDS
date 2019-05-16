import pandas as pd
df = pd.read_csv("diamonds.csv")
df.head()

df_sub = df.loc[:5, "x":]
df_sub["obs"] = df_sub.index
df_sub

df_sub.melt(id_vars = "obs")
df_sub.melt(id_vars = "obs", var_name = "shape", value_name = "cm")

#%%
df = pd.read_csv("traffic_highway.csv")
df.head()

df_melt = df.melt(id_vars = ["date", "StartPoint"],
                  var_name = "EndPoint", 
                  value_name = "traffic")
df_melt.head()

#%%
df = pd.read_csv("diamonds.csv")
df.head()

### clarity 가 2로 끝나는 경우를 추출. ###
set(df["clarity"])

# 1) 
df_sub = df.loc[df["clarity"].str.contains("2$", regex = True), :]
df_sub.head()
set(df_sub["clarity"])

# 2)
df.index = df["clarity"]
df_sub = df.filter(regex = "2$", axis = 0)
df_sub.head()
set(df_sub["clarity"])

# 3)
df.index = df["clarity"]
df_sub = df.filter(regex = "2$", axis = 0).reset_index(drop = True)
df_sub.head()

### clarity 변수의 영문을 제거해보자! ###
# 1)
df["clarity"].str.replace("[A-Z]", "")

# 2)
df["clarity"].str.replace("[^0-9]", "") # 숫자 제외 모두 제거

# 3)
df["clarity"].str.extract("([0-9])")

#%%
from datetime import datetime as dt
tm_now = dt.now()
tm_now.year
tm_now.month
tm_now.weekday()

#%%
dt.strptime("@#2019!!12@@28", "@#%Y!!%m@@%d")

pd.to_datetime([44000, 43000], unit = "D", origin = "1900-01-01")
            

#%%
import pandas as pd
df = pd.read_csv("bike.csv")
df["datetime"] = pd.to_datetime(df["datetime"])
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month
df["hour"] = df["datetime"].dt.hour
df["wday"] = df["datetime"].dt.dayofweek
df.head()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("bike.csv")
df = df.iloc[:200, :]
df.head()

df["casual_MA_5" ] = df["casual"].rolling(window = 5).mean()
df["casual_MA_10"] = df["casual"].rolling(window = 10).mean()
df["casual_MA_24"] = df["casual"].rolling(window = 24).mean()
df["casual_MA_48"] = df["casual"].rolling(window = 48).mean()

plt.plot(df["datetime"], df["casual"      ], color = "#FFAACC")
plt.plot(df["datetime"], df["casual_MA_5" ], color = "#000000")
plt.plot(df["datetime"], df["casual_MA_10"], color = "#FF0000")
plt.plot(df["datetime"], df["casual_MA_24"], color = "#00FF00")
plt.plot(df["datetime"], df["casual_MA_48"], color = "#0000FF")
plt.show()

df["casual"].ewm(alpha = 0.3).mean()

#%%
import pandas as pd
df = pd.read_excel("iris_xlsx.xlsx")
df.head()

std_0 = df.iloc[:, 0].std() # Sepal.Length
std_0
std_1 = df.iloc[:, 1].std() # Sepal.Width
std_1

std_0 / df.iloc[:, 0].mean() # CV - Sepal.Length
std_1 / df.iloc[:, 1].mean() # CV - Sepal.Width

#%%
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report
aa = [1, 1, 0, 0, 1, 1, 1]
bb = [0, 1, 0, 0, 1, 0, 1]

print(classification_report(aa, bb, 
                            target_names=['class 0', 'class 1']))

confusion_matrix(aa, bb)
accuracy_score(aa, bb)
recall_score(aa, bb)
precision_score(aa, bb)

import sklearn.metrics as skm
#skm.accuracy_score()
#skm.recall_score()

#%%
from scipy.stats.stats import pearsonr
import pandas as pd
df = pd.read_excel("iris_xlsx.xlsx")

stat, pvalue = pearsonr(df["Sepal.Length"], df["Sepal.Width"])
round(stat, 2)
round(pvalue, 4)

df.corr(method = "pearson")
df.corr(method = "kendall") # 순위 상관계수(순서형 데이터)
df.corr(method = "spearman") # 순위 상관계수(순서형 데이터)

#%%
from scipy.stats import stats
import pandas as pd
df = pd.read_excel("iris_xlsx.xlsx")
stats.skew(df.iloc[:, 0])
stats.kurtosis(df.iloc[:, 0])

# 제곱근의 계산
import math
math.sqrt(4)
4 ** 0.5

#%%
df = pd.read_excel("iris_xlsx.xlsx")
df[["Sepal.Length", "Sepal.Width"]].boxplot()

#%%
import pandas as pd
from scipy.stats import f_oneway
df = pd.read_excel("iris_xlsx.xlsx")
stat, p = f_oneway(df["Sepal.Length"], 
                   df["Sepal.Width"],
                   df["Petal.Length"])
   
from statsmodels.stats.multicomp import pairwise_tukeyhsd as hsd
posthoc = hsd(df["Sepal.Length"], df["Species"], alpha = 0.05)
print(posthoc)

df = pd.read_csv("diamonds.csv")
posthoc = hsd(df["price"], df["cut"], alpha = 0.05)
print(posthoc)

df.head()
posthoc = hsd(df["carat"], df["color"], alpha = 0.05)
print(posthoc)

#%%
import pandas as pd
import statsmodels.formula.api as smf
df = pd.read_csv("linear_regression_01.csv")
model = smf.ols("y ~ x", data = df)
result = model.fit()
print(result.summary())
