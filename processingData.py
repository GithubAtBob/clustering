import pandas as pd
from time import strptime,mktime
from datetime import datetime
from sklearn.preprocessing import scale
from sklearn.preprocessing import LabelEncoder
import getDistance

def process():
    dFrame = pd.read_csv("processedData.csv")
    dFrame = dFrame.drop(['Unnamed: 0','乘客ID', '出发地详细地址', '目的地详细地址', '目的地坐标经纬度', '服务司机id', '下车时间'], axis=1)
    data = dFrame[~(dFrame['派车时司机坐标经纬度'].isin(['0,0', ',']))]
    data = data[data['订单状态'].isin([100, 23]) & data['订单类型'].isin([0, 1]) & (data['下单时间'] == data['预约时间'])]
    data = data.dropna()

    setOutPlace = data['出发地坐标经纬度'].tolist()
    dPlace = data['派车时司机坐标经纬度'].tolist()
    distance = []
    for i in range(len(setOutPlace)):
        distance.append(getDistance.haversine(
            float(setOutPlace[i].split(',')[0]), \
            float(setOutPlace[i].split(',')[1]), \
            float(dPlace[i].split(',')[0]), \
            float(dPlace[i].split(',')[1])
        ))
    data['司机坐标与出发地距离'] = distance

    data['下单星期'] = data.apply(
        lambda x: datetime.fromtimestamp(mktime(strptime(x['下单时间'], "%Y-%m-%d %H:%M:%S"))).weekday(), axis=1)
    data['下单小时'] = data.apply(lambda x: datetime.fromtimestamp(mktime(strptime(x['下单时间'], "%Y-%m-%d %H:%M:%S"))).hour,
                              axis=1)
    data['派车-预约'] = data.apply(lambda x: int(mktime(strptime(x['派车时间'], "%Y-%m-%d %H:%M:%S"))) - int(
        mktime(strptime(x['预约时间'], "%Y-%m-%d %H:%M:%S"))), axis=1)

    data = data.drop(['出发地坐标经纬度', '派车时司机坐标经纬度', '预约时间', '下单时间', '派车时间', '上车时间', '最终时间（取消/完成）','线路ID','订单状态'], axis=1)

    lbEn = LabelEncoder()
    lbEn.fit(list(data['车型'].values))
    data['车型'] = lbEn.transform(list(data['车型'].values))
    result = data
    print(result.columns)
    result = result.to_numpy()
    result = scale(result)
    print(result)
    return result