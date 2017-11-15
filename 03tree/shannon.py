# encoding: utf-8 
from math import log

def loadData():
  fr =open("lenses.txt")
  lenses =[ inst.strip().split('\t') for inst in fr.readlines()]
  labelLenses=['age','prescript','astigmatic','tearRate']
  return lenses,labelLenses

# {'tearRate': 
#   {'reduced': 'no lenses', 
#    'normal': 
#     {'astigmatic':
#      {'yes': 
#        {'prescript': 
#          {'hyper': {'age': {'pre': 'no lenses', 'presbyopic': 'no lenses', 'young': 'hard'}}, 
#           'myope': 'hard'}}, 
#       'no': 
#         {'prescript': 
#          {'hyper': 'soft', 
#           'myope': {'age': {'pre': 'soft', 'presbyopic': 'no lenses', 'young': 'soft'}}}}}}}}  
def classify(inputTree,featLabels,testVec):
    print inputTree.keys()
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)

    key = testVec[featIndex]
    print featIndex
    print key
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict): 
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel
    
def calcShannon(dataSet):
# 分类 
# 计算概率

  numEntries = len(dataSet)

  labelCounts ={}
  for featVec in dataSet:
    currentLabel = featVec[-1]
    if(currentLabel not in labelCounts.keys()):
      labelCounts[currentLabel] = 0
      labelCounts[currentLabel] += 1
    else:
      labelCounts[currentLabel] += 1
  

  shanonEnt = 0.0
  for key in labelCounts:
    prob = float(labelCounts[key])/numEntries
    shanonEnt -= prob * log(prob,2)

  return shanonEnt
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): 
        	labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
      if featVec[axis] == value:
          reducedFeatVec = featVec[:axis]     #chop out axis used for splitting
         
          reducedFeatVec.extend(featVec[axis+1:])
          retDataSet.append(reducedFeatVec)
    return retDataSet
def choiceBestInfoGain(dataSet):
    baseEnt = calcShannonEnt(dataSet)
    # 根据特征A划分的集合 计算每一个分割集合的信息熵
    # 按A来分割 求A的种类 axis和value
    numFeature  = len(dataSet[0])-1
    bestInfoGain=0.0;bestFeature =0.0;
    for i in range(numFeature):
      featList =[example[i] for example in dataSet]
      uniqueVals = set(featList)
      newEntropy =0.0
      for value in uniqueVals:
        subDataSet=splitDataSet(dataSet,i,value)
        pro =len(subDataSet)/float(len(dataSet))
        newEntropy +=pro*calcShannonEnt(subDataSet)
      infoGain =  baseEnt-newEntropy
    if(infoGain>bestInfoGain): # 选一个最大的信息增益
       bestInfoGain = infoGain
       bestFeature =i
    return bestFeature
    
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList): 
        return classList[0]#stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1: #stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = choiceBestInfoGain(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree  

def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()
    
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)

















    