import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

dFrame = pd.read_excel("C:\\Users\\a1258\\Desktop\\新建文件夹\\locations_all361000_to_3630001548225058.xlsx")
data = dFrame[~(dFrame['出发地坐标经纬度'].isin(['116.385814,39.871182']))]
data = pd.concat([data,pd.DataFrame(columns=['出发地聚类Id','目的地聚类Id'])])
data = data.reset_index(drop=True)
fLonLat = []
tLonLat = []
fromP = data['出发地坐标经纬度'].tolist()
toP = data['目的地坐标经纬度'].tolist()
for i in range(len(fromP)):
    fLonLat.append([float(fromP[i].split(',')[0]), float(fromP[i].split(',')[1])])
    tLonLat.append([float(toP[i].split(',')[0]), float(toP[i].split(',')[1])])
fLonLat = np.array(fLonLat)
tLonLat = np.array(tLonLat)
n_clusters = 8
kmeansF =KMeans(n_clusters)
kmeansF.fit(fLonLat)
kmeansT =KMeans(n_clusters)
kmeansT.fit(tLonLat)
for index,row in data.iterrows():
    data.loc[index,'出发地聚类Id'] = kmeansF.labels_[index]
    data.loc[index,'目的地聚类Id'] = kmeansT.labels_[index]
data.to_csv('processedData.csv')
colors = ['b','c','g','k','m','r','w','y']
for i in range(n_clusters):
    members = kmeansF.labels_==i
    plt.scatter(fLonLat[members, 0], fLonLat[members, 1], s=60, marker='*', c=colors[i], alpha=0.5)
plt.title(' ')
plt.show()