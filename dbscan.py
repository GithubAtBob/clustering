import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
data = pd.read_excel("C:\\Users\\a1258\\Desktop\\新建文件夹\\聚类原始数据.xlsx")
fLonLat = []
tLonLat = []
fromP = data['出发地坐标经纬度'].tolist()
toP = data['目的地坐标经纬度'].tolist()
for i in range(len(fromP)):
    fLonLat.append([float(fromP[i].split(',')[0]), float(fromP[i].split(',')[1])])
    tLonLat.append([float(toP[i].split(',')[0]), float(toP[i].split(',')[1])])
fLonLat = np.array(fLonLat)
tLonLat = np.array(tLonLat)
dbF =DBSCAN(eps=0.01,min_samples=10).fit_predict(fLonLat)
dbT =DBSCAN(eps=0.02,min_samples=10).fit_predict(tLonLat)
plt.scatter(fLonLat[:,0],fLonLat[:,1],c=dbF)
plt.show()