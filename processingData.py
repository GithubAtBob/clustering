import pandas as pd
from sklearn.preprocessing import scale
from sklearn.preprocessing import LabelEncoder


def t2m(t):
    h,m,s = t.strip().split(":")
    return (int(h) * 3600 + int(m) * 60 + int(s))/60

def process():
    dFrame = pd.read_csv("processedData.csv")
    data = dFrame.drop(['Unnamed: 0', '预约时间', '小时2', '出发地详细地址', '出发地坐标经纬度', '目的地详细地址', '目的地详细地址', \
                        '目的地坐标经纬度', '派车时间'], axis=1)

    timeDiff = data['时差（3个小时以内）'].tolist()
    for i in range(len(timeDiff)):
        timeDiff[i] = t2m(timeDiff[i])
    data['时差（3个小时以内）'] = timeDiff

    lbEn = LabelEncoder()
    lbEn.fit(list(data['天气情况'].values))
    data['天气情况'] = lbEn.transform(list(data['天气情况'].values))

    result = data
    print(result.columns)
    result = result.to_numpy()
    result = scale(result)
    print(result)
    return result