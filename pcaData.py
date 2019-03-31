import processingData
from sklearn.decomposition import PCA

def pca():
    dataSet = processingData.process()
    pca = PCA(n_components=0.9)
    newData = pca.fit_transform(dataSet)
    print(pca.explained_variance_ratio_)
    return newData
