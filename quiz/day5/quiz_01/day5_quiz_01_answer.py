#Q1. pandas 모듈을 pd로 불러오시오.
import pandas as pd

#Q2. "bike_weather.csv"를 pandas 모듈을 활용하여 불러오고 객체 종류를 확인하시오
#(단, df 객체에 저장하시오)
df = pd.read_csv("bike_weather.csv")

#Q3. df의 첫 5개 row를 출력하시오
df.head()

#Q4. "date"와 "hour"변수를 활용하여 "time" 변수를 생성하시오
#(예시, 2011-01-01 00:00:00) ※ .astype(), .join() 활용 추천
type(df["hour"])
type(df["hour"][0])

df["time"] = df[["date", "hour"]].apply(lambda x: " ".join(x), axis = 1)
# !?!?

df["hour"] = df["hour"].astype(str)

# 1)
df["time"] = df[["date", "hour"]].apply(lambda x: " ".join(x), axis = 1)

from datetime import datetime as dt
df["time"] = df["time"].apply(lambda x: dt.strptime(x, "%Y-%m-%d %H"))
df.head()
type(df["time"][0])

# 2) 
df["time"] = df[["date", "hour"]].apply(lambda x: x[0] + " " + x[1] + ":00:00", axis = 1)
type(df["time"][0])
df["time"] = pd.to_datetime(df["time"])
type(df["time"][0])

# ※ join 예제
aa = "aaaa"
aa.join("ddddd")
aa.join(["1", "2", "3"])
" ".join(["2011-01-01", "12"])

#Q5. df 객체에서 "date" 변수를 제거하시오.
df.columns
# 1)
df = df.iloc[:, 1:]

# 2)
df = df.drop("date", axis = 1)

df.columns

#Q6. "time" 변수 활용하여 요일 변수 "wday"를 생성하시오.
df["wday"] = df["time"].dt.weekday
df.head()

#Q7. 주중: 0, 주말: 1 의 값을 가지는 "wend" 변수를 생성하시오.
# 1)
df["wend"] = (df["wday"] >= 5) + 0
pd.crosstab(df["wday"], df["wend"])

# 2)
import numpy as np
df["wend"] = np.where(df["wday"] >= 5, 1, 0)
pd.crosstab(df["wday"], df["wend"])

#Q8. "bike_rental.csv"에 있는 자전거 대여랑[count] 정보를 
#     df 객체에 [count] 라는 변수명으로 추가하시오.
rental = pd.read_csv("bike_rental.csv")
rental.head()

rental["datetime"] = pd.to_datetime(rental["datetime"])
df = pd.merge(df, rental[["datetime", "count"]],
              left_on = "time", right_on = "datetime")
df.head()

#Q9. 주중과 주말에 따른 [count]의 차이가 있는지 검정하고, 
#    검정 결과에 포함된 검정통계량의 절대값을 반올림 하여 소수점 셋째 자리 까지 표기하시오.
import scipy.stats as ss
df.columns

ss.ttest_ind(df.loc[df["wend"] == 0, "count"],
             df.loc[df["wend"] == 1, "count"])

stat, p = ss.ttest_ind(df.loc[df["wend"] == 0, "count"],
                       df.loc[df["wend"] == 1, "count"])
round(abs(stat), 3)

#Q10. 월~금 데이터를 따로 떼어내어 df_sub에 저장하시오.
df_sub = df.loc[df["wend"] == 0, :]
df_sub["wday"].value_counts()
df_sub["wday"].unique()
set(df_sub["wday"])

#Q11. df_sub의 데이터를 참고하여 요일에 따른 이용자의 평균 자전거 이용[count] 차이가 있는지 검정하고, 검정 결과에 포함된 검정통계량을 반올림 하여 소수점 셋째 자리 까지 표기하시오.
stat, p = ss.f_oneway(df_sub.loc[df_sub["wday"] == 0, "count"],
                      df_sub.loc[df_sub["wday"] == 1, "count"],
                      df_sub.loc[df_sub["wday"] == 2, "count"],
                      df_sub.loc[df_sub["wday"] == 3, "count"],
                      df_sub.loc[df_sub["wday"] == 4, "count"])
round(stat, 1)
# 'count ~ C("wday")'
p

#Q12. 직전의 검정에 대하여 사후검정을 실시하고 그 결과를 해석하시오.
from statsmodels.stats import multicomp
result = multicomp.pairwise_tukeyhsd(df_sub["count"], df_sub["wday"])
print(result)

