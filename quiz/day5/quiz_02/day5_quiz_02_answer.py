#Q1. pandas 모듈을 pd로 불러오시오.
import pandas as pd

#Q2. "bank.csv"를 pandas 모듈을 활용하여 불러와서 df 객체에 저장하시오.
#(단, 구분자에 유의)
df = pd.read_csv("bank.csv", sep = ";")

#Q3. df의 첫 5개 row를 출력하시오
df.head()

#Q4. [y] 변수의 "no"는 0, "yes"는 1로 변환하시오.
# 1)
df["y"] = (df["y"] == "yes") + 0
set(df["y"])

# 2)
df["y"] = df["y"].replace("no", 0).replace("yes", 1)

#Q5. [job] 변수의 원소 비율을 계산하여 jobs 객체에 저장하시오.
jobs = df["job"].value_counts(normalize = True)
jobs

#Q6. jobs 객체에서 원소 비율이 5% 미만인 원소만 추출하여 jobs 객체에 저장하시오.
jobs < 0.05
jobs[jobs < 0.05]
jobs[jobs < 0.05].index
jobs = jobs[jobs < 0.05].index

#Q7. jobs 객체를 활용하여 df 객체의 [jobs] 변수의 원소 중 비율이 5% 미만인 원소를 전부 "etc"로 치환하시오.
# 1)
df.columns
for s in jobs:
    df["job"] = df["job"].replace(s, "etc")

# 2)
import numpy as np
df["job"] = df["job"].apply(lambda x: np.where(x in jobs, "etc", x))

#Q8. [job] 변수의 원소 비율을 확인하고, 
#    원소 etc의 비율을 반올림하여 소수점 셋째 자리까지 기술하시오.
df["job"].value_counts(normalize = True)
df["job"].value_counts(normalize = True)["etc"]

# 1)
round(df["job"].value_counts(normalize = True)["etc"], 3)

# 2)
df["job"].value_counts(normalize = True)["etc"].round(3)


#Q9. df 객체의 [job] 변수의 가변수를 생성하여 dummy_job 에 저장하시오.
#(단, 생성되는 가변수의 접두사는 "job"으로 설정한다.)
dummy_job = pd.get_dummies(df["job"], prefix = "job")
dummy_job.head()

#Q10. df 객체의 [y], [age], [balance], [duration], [previous] 변수를 추출하여 df2 객체에 저장하시오.
df2 = df[["y", "age", "balance", "duration", "previous"]]

#Q11. df2 객체의 첫 5개 row를 출력하시오.
df2.head()

#Q12. df2 객체와 dummy_job 변수를 concat() 함수를 활용하여 병합하시오.
df2 = pd.concat([df2, dummy_job], axis = 1)

#Q13. df2 객체의 column명을 확인하시오.
df2.columns

#Q14. df2 객체의 "balance" 변수의 기술통계량을 확인하시오.
df2["balance"].describe()

#Q15. df2 객체의 "balance" 변수의 값이 음수이면 1이고 나머지는 0인 변수 [is_minus] 변수를 df2 객체에 추가하시오.
# 1)
df2["is_minus"] = (df2["balance"] < 0) + 0

# 2)
df2["is_minus"] = np.where(df2["balance"] < 0, 1, 0)

#Q16. df2 객체의 "balance" 변수를 5000 단위로 구간화 하시오.
#(예시. 0 -> 0, 2345 -> 1 5123 -> 2)
df2.loc[df2["balance"] <= 0, "balance"] = -1
df2["balance"] = (df2["balance"] // 5000) + 1
set(df2["balance"])

(2345 // 5000) + 1
(-1 // 5000) + 1

#Q17. df2 객체를 사용하여 종속변수를 [y], 나머지 변수를 독립변수로 지정하여 
#     logistic regression을 실시하시오.
import sklearn.metrics as skm
from sklearn.linear_model import LogisticRegression as lr

df2.head()

model = lr().fit(df2.iloc[:, 1:], df2["y"])
print(model)
model.coef_

pred = model.predict_proba(df2.iloc[:, 1:])[:, 1] # [:, 0]

df_result = pd.DataFrame({"y_true": df2["y"],
                          "y_pred": np.where(pred > 0.5, 1, 0)})

skm.accuracy_score(df_result["y_true"], df_result["y_pred"])
skm.recall_score(df_result["y_true"], df_result["y_pred"])
skm.precision_score(df_result["y_true"], df_result["y_pred"])
skm.f1_score(df_result["y_true"], df_result["y_pred"])
skm.roc_auc_score(df_result["y_true"], df_result["y_pred"])
    
import statsmodels.api as sm
model_sm = sm.Logit(df2["y"], df2.iloc[:, 1:])
result = model_sm.fit()
result.summary()

