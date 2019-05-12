import pandas as pd
df = pd.read_csv("class_scores.csv")
df = df.iloc[:3, 4:9]
ser = pd.Series([2, 2, 4, 2, 6])

# 1)
df_ser = pd.DataFrame(ser).T
df_ser.columns = df.columns
df_ser

# 2)
df_ser = pd.DataFrame([ser])
df_ser.columns = df.columns
df_ser
