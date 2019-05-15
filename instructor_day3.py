#%%
import numpy as np
import pandas as pd
df = pd.read_csv("iris_missing.csv")
df_sub = df.head()

df["Sepal.Length"].mean()
np.mean(df["Sepal.Length"])
np.nanmean(df["Sepal.Length"])

df["Sepal.Width"].mean()
np.mean(df["Sepal.Width"])
np.nanmean(df["Sepal.Width"])

df_sub.fillna(999)
df_sub["Sepal.Width"].fillna(999)

#%%

df_sub["Sepal.Width"].fillna(df_sub["Sepal.Width"].mean())

#%%
df_mis = df.iloc[5:9, 0:-1]
df_mis

#df.iloc[5:9, 0:4]
#df.iloc[5:9, 0:-1]
#df.iloc[5:9, :-1]

df_mis.dropna()
df_mis.dropna(how = "any")
df_mis.dropna(how = "all")

df_mis[df_mis["Sepal.Width"].isnull()]
df_mis[df_mis["Petal.Length"].isnull()]
sum(df_mis["Sepal.Width"].isnull())
sum(df_mis["Sepal.Width"].notnull())

df_mis.apply(lambda x: sum(x.isnull())) # column별 결측치 개수
df_mis.apply(lambda x: sum(x.isnull()), axis = 1) # row ~

df_mis.apply(lambda x: sum(x.isnull())).sum() # 전체 결측치 개수

df.boxplot()
df.hist()

#%%
import pandas as pd
df = pd.read_csv("bike.csv")
df["casual"].max()
df["casual"].quantile(0.99)
df["casual"].quantile(0.01)
df_sub = df.loc[df["casual"] >= df["casual"].quantile(0.99), :]

sum(df["casual"] >= df["casual"].quantile(0.99))

#%%
text = "aaBcde"
len(text)
text.upper()
text.find("aa")
text.find("aB")
text.find("B")
text.find("b")

text.find("b") != -1
text.find("B") != -1

#%%
runfile("./hello.py")
udf_01("Hello!")

#%%
dd = [2, 4, 3, 1]
type(dd)

#dd = dd.sort() # XXXX
dd.sort()
dd

dd.sort(reverse = True)
dd

df = pd.read_csv("bike.csv")
df.head()
df_sub = df.iloc[:6, 9:12]
df_sub

#%%
df = pd.read_csv("diamonds.csv")
df.head()

df_sub = df.loc[:, "price":]
df_sub.head()

df_sub.agg(["sum", "min"])
df_sub.describe()

#%%
df = pd.read_csv("bike.csv")
df_1 = df.head()
df_2 = df.tail()

pd.concat([df_1, df_2], axis = 1)
pd.concat([df_1, df_2.reset_index(drop = True)], axis = 1)

#%%
df_list = pd.read_csv("join_list.csv", encoding = "CP949")
df_room = pd.read_csv("join_room.csv", encoding = "CP949")

df_list.head(2)
df_room.head(2)

df_list.join(df_room, how = "left")
df_list.join(df_room, how = "inner")

df_list_sub = df_list.iloc[9:14, :].reset_index(drop = True)
df_list_sub.join(df_room, how = "left")

df_list.merge(df_room, how = "left",
              left_on = "member", right_on = "name")

#%%
import pandas as pd
df = pd.read_csv("diamonds.csv")
df.head(2)

df_cut_dummy = pd.get_dummies(df["cut"], prefix = "cut")
df_cut_dummy.head(7)
df["cut"].iloc[:7]

df_cut_dummy = pd.get_dummies(df["cut"], prefix = "cut", 
                              drop_first = True)
df_cut_dummy.head(7)

price = df["price"]
price.hist()
price.quantile([0, 1])

df["price"] = (price - min(price)) / (max(price) - min(price))
df["price"].hist()
df["price"].quantile([0, 1])

depth = df["depth"]
depth.hist()

df["depth"] = (depth - depth.mean()) / depth.std()
df["depth"].hist()

#%%
import re
import pandas as pd

# 실습데이터 만들기
text1 = "1234 asdfASDF  ㄱㄴㄷㄹㅏㅑㅓㅕ가나다라   .!@#"
text2 = "<a> <ab> <abc> <abcd>"
text3 = pd.Series(["aaa", "bbb", "ccc", "abc"])

# text1
# 숫자 치환
re.sub(pattern = "[0-9]", repl = "@", string = text1)

# 영문 치환
# __ 소문자 치환
re.sub(pattern = "[a-z]", repl = "@", string = text1)

# __ 대문자 치환
re.sub(pattern = "[A-Z]", repl = "@", string = text1)

# 한글 치환
# __ 자음 치환
re.sub(pattern = "[ㄱ-ㅎ]", repl = "@", string = text1)

# __ 모음 치환
re.sub(pattern = "[ㅏ-ㅣ]", repl = "@", string = text1)

# __ 완성형 치환
re.sub(pattern = "[가-힣]", repl = "@", string = text1)

# 띄어쓰기 치환
re.sub(pattern = " ", repl = "@", string = text1)
re.sub(pattern = "  ", repl = "@", string = text1)
re.sub(pattern = "   ", repl = "@", string = text1)


# 응용
# __ 숫자가 아닌 모든 문자 치환
re.sub(pattern = "[^0-9]", repl = "@", string = text1)
re.sub(pattern = "[^0-9]", repl = "", string = text1)

# __ 영문자가 아닌 모든 문자 치환
re.sub(pattern = "[^A-za-z]", repl = "@", string = text1)
re.sub(pattern = "[^A-z]", repl = "@", string = text1)

# __ 한글이 아닌 모든 문자 치환
re.sub(pattern = "[^ㄱ-힣]", repl = "@", string = text1)

# __ 숫자와 영문 대문자가 아닌 모든 문자 치환
re.sub(pattern = "[^0-9A-Z]", repl = "@", string = text1)

# __ 숫자 2, 3만 치환
re.sub(pattern = "[2-3]", repl = "@", string = text1)
re.sub(pattern = "[23]", repl = "@", string = text1)
re.sub(pattern = "2|3", repl = "@", string = text1)

re.sub(pattern = "[23]", repl = "@", string = "255553")

# __ 숫자 2, 3, 4, 7, 8, 9 치환
re.sub(pattern = "2|3|4|7|8|9", repl = "@", string = text1)
re.sub(pattern = "[2-47-9]", repl = "@", string = text1)

# __ '.'의 치환
re.sub(pattern = ".", repl = "@", string = text1)
re.sub(pattern = "\.", repl = "@", string = text1)
re.sub(pattern = "[.]", repl = "@", string = text1)

# __ 두 칸 띄어쓰기와 세 칸 띄어쓰기의 치환
re.sub(pattern = "  |   ", repl = "@", string = text1)
re.sub(pattern = " {2}| {3}", repl = "@", string = text1)
re.sub(pattern = " {2,3}", repl = "@", string = text1)

re.sub(pattern = " {2,}", repl = " ", string = text1)

re.sub(pattern = "[a-z]{2}", repl = "@", string = text1)
re.sub(pattern = " [a-z]{2}", repl = "@", string = text1)

# __ "asdf"와 "가나다라" 치환
re.sub(pattern = "asdf|가나다라", repl = "@", string = text1)
re.sub(pattern = "asdf|[가-라]", repl = "@", string = text1)
re.sub(pattern = "asdf|[가-라]{1}", repl = "@", string = text1)
re.sub(pattern = "asdf|[가-라]{4}", repl = "@", string = text1)

# 특수문자내 문자 처리(text2)
# __ 모든 경우의 수 치환
re.sub(pattern = "<.*?>", repl = "@", string = text2)

# __ 내부 문자 1개 치환
re.sub(pattern = "<.>", repl = "@", string = text2)
re.sub(pattern = "<.{1}>", repl = "@", string = text2)
re.sub(pattern = "<[a-z]>", repl = "@", string = text2)
re.sub(pattern = "<[a-z]{1}>", repl = "@", string = text2)

# __ 내부 문자 2~4개 치환
re.sub(pattern = "<.{2,4}>", repl = "@", string = text2)

# 텍스트 조건(text3)
# __ "a"를 포함하는 원소 추출
text3.str.match(pat = "a")
text3[text3.str.match(pat = "a")]

# __ "b"를 포함하는 원소 추출
text3.str.match(pat = "b")

# __ "b"로 시작하는 원소 추출
text3.str.match(pat = "^b")

# __ "a"로 끝나는 원소 추출
text3.str.match(pat = "a$")
text3.str.match(pat = "^.*a$")
text3.str.match(pat = "^.*?a$")

# __ "a"또는 "b"를 포함하는 원소 추출
text3.str.match(pat = "a|b")

text3.str.match(pat = "^[0-9]{8}_SDS")
# 20190515_SDS_edu.csv

text3.str.match(pat = "^.*?csv$")

#%%
f = open("naver_source_190204.txt")
tx = f.readlines()
f.close()

"ah_k" in tx[457]
# 1)
for s in tx:
    if "ah_k" in s:
        print(s)

len('<span class="ah_k">')
len('</span>')

# 2)
for s in tx:
    if "ah_k" in s:
        print(s[19:-8])

# 3)
keys = []
for s in tx:
    if "ah_k" in s:
        keys.append(s[19:-8])
keys

# 4) list comprehension
keys = [s[19:-8] for s in tx if "ah_k" in s]

keys[:20]
