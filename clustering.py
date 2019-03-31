import pandas as pd
import processingData
from sklearn.cluster import KMeans

dataSet = processingData.process()
kmeans =KMeans(n_clusters=6)
kmeans.fit(dataSet)
dFrame = pd.read_excel("C:\\Users\\a1258\\Desktop\\新建文件夹\\聚类原始数据.xlsx")
data = pd.concat([dFrame,pd.DataFrame(columns=['聚类结果Id'])])
for index,row in data.iterrows():
    data.loc[index,'聚类结果Id'] = kmeans.labels_[index]
data.to_csv('resultData.csv')