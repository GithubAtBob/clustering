import pcaData
from sklearn.cluster import KMeans


dataSet = pcaData.pca()
kmeans =KMeans(n_clusters=5)
kmeans.fit(dataSet)
print("Cluster memberships:\n{}".format(kmeans.labels_[0:1000]))