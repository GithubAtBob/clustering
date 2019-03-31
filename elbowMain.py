import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import processingData

dataSet = processingData.process()

n_clusters = range(1, 10)
meandistortions = []

for k in n_clusters:
    kmeans = KMeans(k)
    kmeans.fit(dataSet)
    meandistortions.append(sum( \
        np.min(cdist(dataSet, kmeans.cluster_centers_, 'euclidean'), axis=1)) / dataSet.shape[0])

plt.plot(n_clusters, meandistortions, 'bx-')
plt.xlabel('k')
plt.ylabel('average distortion degree')
plt.title('elbowMethod for the best K')
plt.show()