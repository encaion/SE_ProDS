#Q1. pandas 모듈을 pd로 불러오시오.
import pandas as pd

#Q2. "hotel_booking_train_1m.csv"를 pandas 모듈을 활용하여 불러오고 객체 종류를 확인하시오.
#(불러온 파일을 df 객체에 저장하시오.)
df = pd.read_csv("hotel_booking_train_1m.csv")

#Q3. df 객체의 첫 5개 row를 출력하시오.
df.head()

#Q4. df 객체의 마지막 2개 row를 출력하시오.
df.tail(2)

#Q5. df 객체의 차원을 확인하시오.
df.ndim

#Q6. df 객체의 row와 column개수를 확인하시오.
df.shape

#Q7. df 객체의 column 이름을 확인하시오
df.columns

#Q8. df 객체의 [user_location_country] 변수명을 [country]로, [user_location_city] 변수명을 [city]로 변경하시오.
df.rename(columns = {"user_location_country": "country",
                     "user_location_city": "city"}, inplace = True)
df.columns

#Q9. 국가[country]별 도시[city] 개수를 센 결과를 df_co 변수에 저장하시오.
#(국가 번호 0의 도시 개수는 205개 이다.)
set(df["country"])
df.loc[df["country"] == 0, "city"].unique() # 1
set(df.loc[df["country"] == 0, "city"]) # 2

len(set(df.loc[df["country"] == 0, "city"]))

df_co = df[["country", "city"]].groupby("country").agg(lambda x: len(set(x)))
df_co

def uni(x):
    return len(set(x))

df[["country", "city"]].groupby("country").agg(uni)

#Q10. df 객체에서 각 사이트[site_name]의 빈도를 계산하여 site_counts 변수에 저장하시오.
#(사이트 번호 2의 빈도는 631617번 이다.)
site_counts = df["site_name"].value_counts()
site_counts.head()

#Q11. site_counts를 참고하여 빈도 상위 10개 사이트를 확인하고 해당 사이트를 기준으로 df 객체에서 데이터를 추출하시오.
#(단, 추출한 데이터는 df_sub에 저장한다.)
site_counts[:10].index
df_sub = df.loc[df["site_name"].isin(site_counts[:10].index), :]
df_sub.head()
df_sub["site_name"].value_counts()
len(set(df_sub["site_name"]))

#Q12. df_sub 객체를 참고하여 검색시 입력한 숙박 인원수(성인)[srch_adults_cnt]에 따른 예약[is_booking]비율을 book_ratio에 저장하시오.
book_ratio = df_sub[["srch_adults_cnt", "is_booking"]].groupby("srch_adults_cnt").agg("mean")
book_ratio = df_sub[["srch_adults_cnt", "is_booking"]].groupby("srch_adults_cnt").mean()

dd = df_sub.loc[df_sub["srch_adults_cnt"] == 1, ["srch_adults_cnt", "is_booking"]]
sum(dd["is_booking"] == 1) / len(dd)


#Q13. book_ratio를 참고하여 가장 예약 비율이 높은 성인의 숙박 인원수를 기술하시오.
book_ratio.idxmax()
