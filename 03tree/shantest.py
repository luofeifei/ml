# encoding: utf-8 
import copy
from numpy import * 
import shannon
import treePlot
# dataSet =[[1,1,'yes'],
#           [1,1,'yes'],
#           [1,0,'no'],
#           [0,1,'no'],
#           [0,1,'no']]
# labels=['no surfacing','flippers']

dataSet,labels = shannon.loadData()
labeles = [ value for value in labels]
#shannon.calcShannonEnt(dataSet)
#print shannon.calcShannon(dataSet)

#print shannon.splitDataSet(dataSet,0,1)
#print shannon.choiceBestInfo(dataSet)
#{'flippers': {0: 'no', 1: {'no surfacing': {0: 'no', 1: 'yes'}}}}
#tree = shannon.createTree(dataSet,labels)


#shannon.storeTree(tree,'test.txt')
treep = shannon.grabTree("test.txt")
#treePlot.createPlot(treep)
#print shannon.classify(tree,labeles,[0,0])
#print shannon.classify(treep,labeles,['young','myope','no','reduced'])
print shannon.classify(treep,labeles,['young','hyper','yes','normal'])
#print shannon.classify(treep,labeles,['young','myope','no','normal'])




