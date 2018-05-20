#!/usr/bin/env python3

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn import tree

#DEFINING IRIS CONSTRUCTOR
dia=load_diabetes()

#LOADING IRIS DATA
data=dia.data.tolist()
target=dia.target.tolist()

#SEPERATING TRAINING & PREDICT DATA
predict_data=data[441]
del data[441]
del target[441]

training_target=target
training_data=data

#APPLYING ALGOTITHM
algo=tree.DecisionTreeClassifier()

trained=algo.fit(training_data,training_target)

result1 = trained.predict([predict_data])

print(result1)

