# -*- coding: UTF-8 -*-
import numpy as np
import operator
"""
函数说明:创建数据集
 
Parameters:
    无
Returns:
    group - 数据集
    labels - 分类标签
"""


def creatdataset():
    # 四组二维特征
    group = np.array([[1, 101], [5, 89], [108, 5], [115, 8]])
    # 四组特征的标签
    labels = [' 爱情片', ' 爱情片', '动作片', '动作片']
    return group, labels


"""
函数说明:kNN算法,分类器
 
Parameters:
    inX - 用于分类的数据(测试集)
    dataSet - 用于训练的数据(训练集)
    labels - 分类标签
    k - kNN算法参数,选择距离最小的k个点
Returns:
    sortedClassCount[0][0] - 分类结果
"""


def classify(inx, dataset, labels, k):
    datasetsize = dataset.shape[0]
    # numpy函数shape[0]返回dataSet的行数
    diffmat = np.tile(inx, (datasetsize, 1))-dataset
    # 在列向量方向上重复inX共1次(横向)，行向量方向上重复inX共dataSetSize次(纵向)
    sqdiffmat = diffmat**2
    sqdistances = sqdiffmat.sum(axis=1)
    # axis=1 每一行的元素相加
    distances = sqdistances**0.5
    # 计算距离完成
    print(distances)
    sortedDistIndices = distances.argsort()
    print(sortedDistIndices)
    # 返回distances中元素从小到大排序后的索引值
    classcount = {}
    # 定义一个记录类别次数的字典
    for i in range(k):
        print(i)
        votelabel = labels[sortedDistIndices[i]]
        print(votelabel)
        classcount[votelabel] = classcount.get(votelabel, 0)+1
        # dict.get(key,default=None),字典的get()方法,
        # 返回指定键的值,返回的是值value，如果值不在字典中返回默认值。
        print(classcount)
        sortedcalsscount = sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)
        # key=operator.itemgetter(1)根据字典的值进行排序
        # key=operator.itemgetter(0)根据字典的键进行排序
        # reverse降序排序字典
        return sortedcalsscount[0][0]
        # 返回次数最多的类别,即所要分类的类别


if __name__ == '__main__':
    # 作为主程序会执行以下内容，不是主程序不会执行
    group, labels = creatdataset()
    test = [101, 20]
    test_class = classify(test, group, labels, 3)
    print(test_class)
