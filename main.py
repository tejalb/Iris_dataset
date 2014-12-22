from functions import *

trainingSet=[]
testSet=[]
split=0.67
loadDataset('iris.data', split, trainingSet, testSet)
print 'Train set: ' + repr(len(trainingSet))
print 'Test set: ' + repr(len(testSet))

# Predict

predictions=[]
k=3
for item in testSet:
    nbs=getNeighbors(trainingSet, item,k)
    predictions.append(getResponse(nbs))

accuracy=getAccuracy(testSet,predictions)
print 'Accuracy is ' + repr(accuracy)
