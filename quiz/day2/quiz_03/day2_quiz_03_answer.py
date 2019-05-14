#Q1. pandas 모듈을 pd로 불러오시오.
import pandas as pd

#Q2. "traffic_highway.csv"를 pandas 모듈을 활용하여 불러오고 객체 종류를 확인하시오
#(단, df 객체에 저장하시오)
df = pd.read_csv("traffic_highway.csv")

#Q3. df의 첫 5개 row를 출력하시오
df.head()

#Q4. df의 마지막 2개 row를 출력하시오
df.tail(2)

#Q5. df의 차원을 확인하시오
df.ndim

#Q6. df의 row 개수를 확인하시오
len(df)

#Q7. df의 column 개수를 확인하시오
len(df.columns)

#Q8. df의 column 이름을 확인하시오
df.columns

#Q9. 출발지점(StartPoint)과 도착지점(column)의 일 교통량의 최대값을 "max" 라는 이름의 변수에 저장하시오.
df.head(2)
# 1)
df["max"] = df.iloc[:, 2:7].max(axis = 1)

# 2)
df["max"] = df.iloc[:, 2:7].apply(lambda x: max(x), axis = 1)

#Q10. 일별 출발지점별 총 통행량을 "sum" 이라는 이름의 변수에 저장하시오.
#df["sum"] = df.iloc[:, 2:].sum(1)
df["sum"] = df.iloc[:, 2:7].sum(1)

#Q11. [max] 변수를 참고하여 일별 출발지점별 교통량이 가장 많았던 일자와 그 출발지점을 기술하시오.
df["max"].max()

# 1)
df.loc[df["max"] == df["max"].max()]

# 2)
df.loc[df["max"] == df["max"].max(), ["date", "StartPoint"]]

# 3)
df.loc[df["max"] == df["max"].max(), df.columns[:2]]

#Q12. [sum] 변수를 참고하여 일별 출발지점별 교통량이 가장 많았던 일자와 그 출발지점을 기술하시오.
df.loc[df["sum"] == df["sum"].max()]

#Q13. 출발지점별 일 최대 교통량을 구하시오.
#df.loc[:, ["StartPoint", "max"]].groupby("StartPoint").max()
df.loc[:, ["StartPoint", "sum"]].groupby("StartPoint").max()
