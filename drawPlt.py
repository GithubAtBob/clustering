import pandas as pd
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
sns.set()

def t2m(t):
    h,m,s = t.strip().split(":")
    return (int(h) * 3600 + int(m) * 60 + int(s))/60

data = pd.read_csv("resultData.csv")

timeDiff = data['时差（3个小时以内）'].tolist()
for i in range(len(timeDiff)):
    timeDiff[i] = t2m(timeDiff[i])
data['时差（3个小时以内）'] = timeDiff

lbEn = LabelEncoder()
lbEn.fit(list(data['天气情况'].values))
data['天气情况'] = lbEn.transform(list(data['天气情况'].values))

print(data.head())
sns.pairplot(data=data,hue='聚类结果Id',vars=['号数', '天气情况', '小时1', '时差（3个小时以内）', \
                                          '星期', '订单类型'])