import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

def elbow(direction):
    LonLat = []
    if(direction == 'from'):
        P = data['出发地坐标经纬度'].tolist()
    else:
        P = data['目的地坐标经纬度'].tolist()
    for i in range(len(P)):
        LonLat.append([float(P[i].split(',')[0]), float(P[i].split(',')[1])])
    LonLat = np.array(LonLat)

    n_clusters = range(1, 10)
    meandistortions = []

    for k in n_clusters:
        kmeans = KMeans(k)
        kmeans.fit(LonLat)
        meandistortions.append(sum( \
            np.min(cdist(LonLat, kmeans.cluster_centers_, 'euclidean'), axis=1)) / LonLat.shape[0])

    plt.plot(n_clusters, meandistortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('average distortion degree')
    plt.title('elbowMethod for the best K')
    plt.show()

data = pd.read_excel("C:\\Users\\a1258\\Desktop\\新建文件夹\\聚类原始数据.xlsx")
elbow('to')