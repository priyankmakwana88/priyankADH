#!/usr/bin/env python3

import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

#DEFINING IRIS CONSTRUCTOR
iris=load_iris()

#LOADING IRIS DATA
data=iris.data.tolist()
target=iris.target.tolist()

#SEPERATING TRAINING & PREDICT DATA
predict_data_3=data[149]
del data[149]
del target[149]

predict_data_2=data[99]
del data[99]
del target[99]

predict_data_1=data[49]
del data[49]
del target[49]


training_target=target
training_data=data


#print(type(predict_data_1))
#print(predict_data_2)
#print(predict_data_3)
#print(training_data)

algo=tree.DecisionTreeClassifier()

trained=algo.fit(training_data,training_target)

result1 = trained.predict([predict_data_1])
result2 = trained.predict([predict_data_2])
result3 = trained.predict([predict_data_3])
print(result1)
print(result2)
print(result3)
