from numpy import *
import adaboost
# b = 0.5 * log(2.3333333)
# print b
# a = (0.1*exp(-b))/(0.7*ex (-b)+0.3*exp(b))
# print a

datMat,classLabels = adaboost.loadSimpData()
#print adaboost.iterateAda(datMat,classLabels)

d=mat(ones((5,1))/5)
 
#print adaboost.buildStump(datMat,classLabels,d)

weakClassArr,aggClassEst =  adaboost.adaBoostTrainDS(datMat,classLabels)
print adaboost.adaClassify([0,0],weakClassArr)