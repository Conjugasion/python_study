"""
@author Lucas
@date 2018/12/6 22:03

"""
import random
import re
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

pattern1 = r'([1-9]\d{7,10})'
re_QQ = re.compile(pattern1)
QQList = re_QQ.findall("516020608888")
print(QQList)

t1 = (1, )
print(type(t1))

# 主成分分析法
# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# pca = PCA(n_components=1)
# newX = pca.fit_transform(X)
# print(X)
# print(newX)
# print(pca.explained_variance_ratio_)
# print(pca.inverse_transform(newX))

# x = [1.38340578, 2.22189802, 3.6053038, -1.38340578, -2.22189802, -3.6053038]
# y = [0.2935787, -0.25133484, 0.04224385, -0.2935787, 0.25133484, -0.04224385]
# plt.plot(x, y, 'r-o')
# plt.show()

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca1 = PCA(n_components=1)
newX1 = pca1.fit_transform(X)
print(newX1)
# print(type(newPca))

print("**********")
Y = np.array([[-1, -5], [-2, -6], [-3, -1], [1, 4], [2, -1], [3, 4]])
pca2 = PCA(n_components=1)
newX2 = pca2.fit_transform(Y)
print(newX2)
newX3 = pca1.fit_transform(Y)
print(newX3)

