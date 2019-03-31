import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def showPlt(direction):
    colors = ['b', 'c', 'g', 'k', 'm', 'r']
    if(direction == 'from'):
        kmeans = kmeansF
        n_clusters = n_clusters_f
        LonLat = fLonLat
    else:
        kmeans = kmeansT
        n_clusters = n_clusters_t
        LonLat = tLonLat
    for i in range(n_clusters):
        members = kmeans.labels_ == i
        plt.scatter(LonLat[members, 0], LonLat[members, 1], s=60, marker='*', c=colors[i], alpha=0.5)
    plt.title(' ')
    plt.show()
dFrame = pd.read_excel("C:\\Users\\a1258\\Desktop\\新建文件夹\\聚类原始数据.xlsx")
data = pd.concat([dFrame,pd.DataFrame(columns=['出发地聚类Id','目的地聚类Id'])])
fLonLat = []
tLonLat = []
fromP = data['出发地坐标经纬度'].tolist()
toP = data['目的地坐标经纬度'].tolist()
for i in range(len(fromP)):
    fLonLat.append([float(fromP[i].split(',')[0]), float(fromP[i].split(',')[1])])
    tLonLat.append([float(toP[i].split(',')[0]), float(toP[i].split(',')[1])])
fLonLat = np.array(fLonLat)
tLonLat = np.array(tLonLat)
n_clusters_f = 6
n_clusters_t = 3
kmeansF =KMeans(n_clusters_f)
kmeansF.fit(fLonLat)
kmeansT =KMeans(n_clusters_t)
kmeansT.fit(tLonLat)
for index,row in data.iterrows():
    data.loc[index,'出发地聚类Id'] = kmeansF.labels_[index]
    data.loc[index,'目的地聚类Id'] = kmeansT.labels_[index]
data.to_csv('processedData.csv')
showPlt('from')