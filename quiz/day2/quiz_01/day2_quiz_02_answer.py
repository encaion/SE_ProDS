#Q1. pandas 모듈을 pd로, numpy 모듈을 np로 불러오시오.
import pandas as pd
import numpy as np

#Q2. "class_scores.csv"를 pandas 모듈을 활용하여 불러오고 객체 종류를 확인하시오
#(단, df 객체에 저장하시오)
df = pd.read_csv("class_scores.csv")

#Q3. df의 첫 3개 row를 출력하시오
df.head(3)

#Q4. df의 마지막 2개 row를 출력하시오
df.tail(2)

#Q5. df의 차원을 확인하시오
df.ndim

#Q6. df의 row 개수를 확인하시오
df.shape[0]
len(df)

#Q7. df의 column 개수를 확인하시오
df.shape[1]
len(df.columns)

#Q8. df의 column 이름을 확인하시오
df.columns

#Q9. 2학년의 학번, 학년, 성적 전체를 추출하여 df_sub 객체에 저장하시오.
# row filtering - 2학년 추출
# 1)
df_sub = df.loc[df["grade"] == 2, :]

# 2)
df_sub = df[df["grade"] == 2]
df_sub.head(2)
set(df_sub["grade"])

# column filtering - 학번, 학년, 성적 추출
df_sub.columns
# 1) 
df_sub = df_sub.loc[:, ['Stu_ID', 'grade', 
                        'Math', 'English', 'Science',
                        'Marketing', 'Writing']]

# 2)
df_sub = df_sub.iloc[:, [0, 1, 4, 5, 6, 7, 8]]

# 3)
df_sub = df_sub.iloc[:, np.r_[0, 1, 4:9]]

# 4)
df_sub = df_sub.iloc[:, np.r_[:2, 4:9]]
#df_sub = df_sub.iloc[:, np.r_[:2, 4:]] # XXXX

# !?!?
#df_sub = df.loc[df["grade"] == 2, np.r_[:2, 4:9]] # XXXX
df_sub = df.loc[df["grade"] == 2, df.columns[np.r_[:2, 4:9]]]

#Q10. df_sub를 기준으로 학생 개개인의 성적 평균을 계산하고 학번과 같이 "day2_quiz_01_score_avg.csv"로 저장하시오.
df_sub.iloc[:, 2:].mean() # 2학년 학생의 과목 평균
means = df_sub.iloc[:, 2:].mean(axis = 1)

df_mean = pd.DataFrame({"Stu_ID": df_sub["Stu_ID"],
                        "AVG": means})
df_mean.head()

df_mean.to_csv("day2_quiz_01_score_avg.csv", index = False)

# !?!?
#df_sub.iloc[:, 2:].mean()
df_sub.iloc[:, 2:].apply(lambda x: x.mean())
# df_sub.iloc[:, 2:].mean(axis = 1)
df_sub.iloc[:, 2:].apply(lambda x: x.mean(), axis = 1)


#Q11. df_sub를 기준으로 과목별 성적 최고점, 최저점, 표준편차를 계산하고 과목명과 함께 score_stat에 저장하시오.
# std()
df_sub.head()
score_stat = pd.DataFrame({"max": df_sub.iloc[:, 2:].max(),
                           "min": df_sub.iloc[:, 2:].min(),
                           "std": df_sub.iloc[:, 2:].std()})
score_stat

score_stat["subject"] = score_stat.index
score_stat

#Q12. score_stat의 index를 0 ~ 4로 만드시오.
# 1)
score_stat.index = np.arange(5)

# 2)
score_stat = score_stat.set_index(np.arange(5))

# 11 ~ 12 !?!?
score_stat = pd.DataFrame({"max": df_sub.iloc[:, 2:].max(),
                           "min": df_sub.iloc[:, 2:].min(),
                           "std": df_sub.iloc[:, 2:].std()})
score_stat = score_stat.reset_index()
score_stat.rename(columns = {"index": "subject"}, inplace = True)
score_stat

#Q13. score_stat 객체를 "day2_quiz_01_score_stat.csv"로 저장하시오.
score_stat.to_csv("day2_quiz_01_score_stat.csv", index = False)

# extra Question!
# - 학생별로 시험 점수가 70점이 넘는 과목의 개수를 구하시오
True + False
False + False
sum([True, False, False])

df_sub.iloc[0, 2:] > 70
sum(df_sub.iloc[0, 2:] > 70)

df_sub.iloc[:, 2:].apply(lambda x: sum(x > 70), axis = 1)




