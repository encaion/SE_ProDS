#Q1. pandas 모듈을 pd로 불러오시오.
import pandas as pd

#Q2. "hotel_booking_train_1m.csv"를 pandas 모듈을 활용하여 불러오고 객체 종류를 확인하시오
#(단, df 객체에 저장하시오)
df = pd.read_csv("hotel_booking_train_1m.csv")

#Q3. df의 첫 5개 row를 출력하시오
df.head()

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

#Q9. 총 몇 군데의 웹사이트[site_name]에서 데이터가 수집되어있는지 조사하시오.
len(set(df["site_name"]))

#Q10. 총 몇 군데의 대륙[posa_continent]에서 데이터가 수집되어있는지 조사하시오.
len(set(df["posa_continent"]))

#Q11. 가장 많은 국가가 있는 대륙[posa_continent] 번호는 몇 번인가?
#단, 국가의 기준은 [user_location_country] 로 한다.
pd.crosstab(df["user_location_country"], df["posa_continent"])

tab = pd.crosstab(df["user_location_country"], df["posa_continent"])
tab.apply(lambda x: sum(x > 0))
tab.apply(lambda x: sum(x > 0)).max()

tab2 = tab.apply(lambda x: sum(x > 0))
tab2.loc[tab2 == tab2.max()]
tab2.loc[tab2 == tab2.max()].index
tab2.loc[tab2 == tab2.max()].index[0]

tab2.idxmax() # 최대값의 index
tab2.idxmin() # 최소값의 index

#Q12. 유입 채널[channel]과 예약[is_booking]여부 데이터를 기반으로 표(crosstab)을 생성하시오.
pd.crosstab(df["channel"], df["is_booking"])

#Q13. 유입 채널[channel]별 예약[is_booking] 비율을 계산하고 이를 cross 객체에 저장하시오.
#여기부터 cross 객체를 기준으로 문제를 해결하시오.
cross = pd.crosstab(df["channel"], df["is_booking"],
                    normalize = "index")

# FYI
pd.crosstab(df["channel"], df["is_booking"], normalize = "columns")

#Q14. 예약비율이 가장 높은 유입 채널은 몇 번인가?
#(단, 숫자 하나만 출력 되어야 한다.)
cross
cross[1]
cross[1].max()

cross.loc[cross[1] == cross[1].max(), :]
cross.loc[cross[1] == cross[1].max(), :].index[0]

#Q15. 예약 비율이 가장 높은 유입 채널의 예약 비율을 소수점 셋 째 자리까지 반올림하여 구하시오.
#(정답 예시: 0.456)
round(cross[1].max(), 3)
cross[1].max().round(3)

#Q16. 유입 채널별 예약비율 정보를 "day2_quiz_02_info.csv"에 저장하시오.
cross.to_csv("day2_quiz_02_info.csv", index = False)

