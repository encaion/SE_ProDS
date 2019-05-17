import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats import outliers_influence
from patsy import dmatrices
df = pd.read_csv("bike.csv")

df["datetime"] = pd.to_datetime(df["datetime"])
df["wday"] = df["datetime"].dt.dayofweek

# One Hot Encoding: weekday
# dummy_wday = pd.get_dummies(df["wday"], prefix = "wday")
dummy_wday = pd.get_dummies(df["wday"], prefix = "wday", drop_first = True)
dummy_wday.head()

X_sub = df[["season", "holiday", "workingday", "temp", "humidity"]]
X = pd.concat([X_sub, dummy_wday], axis = 1)
X.head()

Y = df["casual"]

model = smf.OLS(Y, X).fit()
model.summary()
# model.predict()

df_vif = pd.DataFrame()
df_vif["VIF"] = [outliers_influence.variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
df_vif["features"] = X.columns
df_vif

features = "+".join(df.columns[1:-3])
y, X = dmatrices("casual ~ " + features, df, return_type = "dataframe")

df_vif = pd.DataFrame()
df_vif["VIF"] = [outliers_influence.variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
df_vif["features"] = X.columns
df_vif

df[["temp", "atemp"]].corr()

#%%
import math
math.exp(2)

# Odds Ratio 계산

#%%
from sklearn.cluster import KMeans
import pandas as pd
df = pd.read_excel("iris_xlsx.xlsx")
X = df.loc[:, :"Petal.Width"]
kmeans = KMeans(n_clusters = 3)
kmeans = kmeans.fit(X)
centeroids = pd.DataFrame(kmeans.cluster_centers_, columns = X.columns)
centeroids

kmeans.labels_

df["cluster"] = kmeans.labels_
pd.crosstab(df["Species"], df["cluster"])

kmeans = KMeans(n_clusters = 3, random_state = 1234)
kmeans = kmeans.fit(X)
centeroids = pd.DataFrame(kmeans.cluster_centers_, columns = X.columns)
centeroids

df["cluster"] = kmeans.labels_
pd.crosstab(df["Species"], df["cluster"])
