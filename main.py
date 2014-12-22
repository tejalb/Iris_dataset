# Compare accuracy of my functions and kNN from sklearn

from functions import *
from sklearn.neighbors import KNeighborsClassifier
#from sklearn import neighbors


trainingSet=[]
testSet=[]
split=0.67
loadDataset('iris.data', split, trainingSet, testSet)
print 'Train set: ' + repr(len(trainingSet))
print 'Test set: ' + repr(len(testSet))

# Predict

predictions=[]
k=5
for item in testSet:
    nbs=getNeighbors(trainingSet, item,k)
    predictions.append(getResponse(nbs))

accuracy=getAccuracy(testSet,predictions)
print 'Accuracy using my functions is ' + repr(accuracy)

neigh=KNeighborsClassifier(n_neighbors=k)

Y_train=[]
for item in trainingSet:
    Y_train.append(item[-1])
    del item[-1]

true_Y=[]
for item in testSet:
    true_Y.append(item[-1])
    del item[-1]

neigh.fit(trainingSet,Y_train)
print 'Accuracy from sklearn is ' + repr(neigh.score(testSet,true_Y)*100)
