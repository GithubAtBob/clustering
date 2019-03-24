import pandas as pd

dFrame = pd.read_excel("C:\\Users\\a1258\\Desktop\\新建文件夹\\locations_all361000_to_3630001548225058.xlsx")
dFrame = dFrame.drop( ['下车时间'], axis=1)
data = dFrame[dFrame['订单状态'].isin([100, 23]) & dFrame['订单类型'].isin([0, 1]) & (dFrame['下单时间'] == dFrame['预约时间'])]
data = pd.concat([data,pd.DataFrame(columns=['时间','活动','caseId'])])
data = data.sample(frac=0.1)
i=0
for index,row in data.iterrows():
    data.loc[index,'时间'] = row['下单时间']
    data.loc[index,'活动'] = '下单'
    data.loc[index,'caseId'] = i
    data=data.append([{'时间':row['派车时间'],'活动':'派车','caseId':i}],ignore_index=True)
    if row['订单状态']==100:
        data=data.append([{'时间':row['上车时间'],'活动':'上车','caseId':i}],ignore_index=True)
        data=data.append([{'时间':row['最终时间（取消/完成）'],'活动':'下车','caseId':i}],ignore_index=True)
    else:
        data=data.append([{'时间':row['最终时间（取消/完成）'],'活动':'取消','caseId':i}],ignore_index=True)
    i=i+1
data=data.drop(['上车时间','下单时间','派车时间','最终时间（取消/完成）','预约时间','订单状态'],axis=1)
data=data[data['活动'].isin(['下单','派车','上车','下车','取消'])]
data.to_csv('result.csv')


