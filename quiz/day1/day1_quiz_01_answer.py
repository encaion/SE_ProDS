#Q1. pandas 모듈을 pd로 불러오시오.
import pandas as pd

#Q2. "rating_chocobar.csv"를 pandas 모듈을 활용하여 불러오고 객체 종류를 확인하시오
#(단, df 객체에 저장하시오)
df = pd.read_csv("rating_chocobar.csv")
df.head(2)
df.iloc[0, :]
type(df)

#Q3. df의 첫 3개 row를 출력하시오
df.head(3)

#Q4. df의 마지막 2개 row를 출력하시오
df.tail(2)

#Q5. df의 차원을 확인하시오
df.ndim

#Q6. df의 row 개수를 확인하시오
df.shape
df.shape[0]
len(df)

#Q7. df의 column 개수를 확인하시오
df.shape[1]
len(df.columns)

#Q8. df의 column 이름을 확인하시오
df.columns

#Q9. df의 첫 번째 변수 명을 "aa"로 변경하시오
# 1)
df = df.rename(columns = {"Company_Maker_if_known": "aa"})
df.columns

# 2)
df.rename(columns = {"aa": "bb"}, inplace = True)
df.columns

# 3)
df.rename(columns = {df.columns[0]: "cc"}, inplace = True)
df.columns

#Q10. df의 첫 번째, 네 번째, 열 번째 row를 추출하여 df_sub1 객체에 저장하시오
# 1)
df_sub1 = df.iloc[[0, 3, 9],]

# 2)
df_sub1 = df.iloc[[0, 3, 9], :]

# 3)
df_sub1 = df.take([0, 3, 9])

#Q11. df의 index 번호가 짝수인 것만 추출하여 df_sub2 객체에 저장하시오
# 1)
len(df)
df_sub2 = df.iloc[2:1795:2,]
df_sub2.head()

# 2)
df_sub2 = df.iloc[2:len(df):2,]
df_sub2.head()

# 3)
df_sub2 = df.iloc[2::2,]
df_sub2.head()

# !?)
df_sub2 = df.iloc[::2,]
df_sub2.head()

#Q12. df_sub1과 df_sub2를 차례대로 병합하여 df_sub 객체에 저장하시오
# 1)
df_sub = pd.concat([df_sub1, df_sub2], axis = 0, sort=False)
df_sub.head()

# 2)
df_sub = df_sub1.append(df_sub2, sort=False)
df_sub.head()

# !?)
pd.concat([df.iloc[:3,], df.iloc[:3,]], axis = 1)
dd = pd.concat([df.iloc[:3,], df.iloc[:3,]], axis = 1)
dd.columns

#Q13. df_sub를 "day1_quiz.csv"로 저장하시오.
df_sub.to_csv("day1_quiz.csv", index = False)
