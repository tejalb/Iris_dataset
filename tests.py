from functions import *

d1=[4,4,3,'a']
d2=[4,4,4,'b']
dist=euclideanDistance(d1,d2,3)
print 'Distance= ' + repr(dist)

train=[[1,1,1,'a'], [2,2,2,'a'], [4,5,3,'c']]
test=[0,0,0,'x']
k=3
nbs=getNeighbors(train,test,k)
clas=getResponse(nbs)
print clas


testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predictions)
print accuracy
