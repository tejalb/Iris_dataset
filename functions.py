import csv
import math
import random
import operator
from collections import defaultdict

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'rb') as csvfile:
            lines = csv.reader(csvfile)
            dataset = list(lines)
            for x in range(len(dataset)-1):
                for y in range(4):
                    dataset[x][y] = float(dataset[x][y])
                if random.random() < split:
                    trainingSet.append(dataset[x])
                else:
                    testSet.append(dataset[x])

def euclideanDistance(v1, v2, length):
    dist=0
    for i in range(length):
        dist += pow(v1[i]-v2[i],2)
    return math.sqrt(dist)


def getNeighbors(trainingSet, test, k):
    dists=[]
    for item in trainingSet:
        d=euclideanDistance(item,test,len(item)-1)
        dists.append((item,d))
    dists.sort(key=operator.itemgetter(1))
    nbs=[]
    for x in range(k):
        nbs.append(dists[x][0])
    return nbs

def getResponse(nbs):
    class_count=defaultdict(int)
    for item in nbs:
        class_count[item[-1]] += 1
    max_class=max(class_count.iteritems(),key=operator.itemgetter(1))[0]
    return max_class


def getAccuracy(testSet, predictions):
    cor=0
    for x,item in enumerate(testSet):
        if item[-1]==predictions[x]:
            cor += 1
    return cor/float(len(testSet))*100.0
