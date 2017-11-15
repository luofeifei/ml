
import smo
from numpy import * 
import matplotlib.pyplot as plt
#help(plt)
# y = 1/(1+(np.e)**(-x))
import datetime
dataArr,labelArr = smo.loadDataSet('testSet.txt')

#dataMatrix = mat(dataArr);
#print dataMatrix[0,:] 
# labelMat = mat(labelArr).transpose();
# b = 0; m,n = shape(dataMatrix);
# alphas = mat(zeros((m,1)));
# iter = 0
# print shape(dataMatrix);
# print shape(labelMat);
# print m
# print shape(alphas);
# print dataArr[0:6]
# print labelArr[0:6]
# fig = plt.figure()

# ax = fig.add_subplot(111)

# index=0;
# for x in dataArr:
#  if(index==len(dataArr)):
#  	break;
#  if(labelArr[index]==1):
#  	ax.scatter(x[0],x[1],marker = 'o',color = 'r',s=50)
#  if(labelArr[index]==-1):
#  	ax.scatter(x[0],x[1],marker = '*',color = 'b',s=60)
#  index=index+1

# #ax.scatter(dataArr[:1],dataArr[:2],s=100,c = 'r',marker = 'o')  
# #plt.annotate('(0,0.5)', xytext=(0.2, 0.5),xy=(0,0.5))
# plt.legend(loc = 'upper right')
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111)


#b,alphas = smo.smoSimple(dataArr,labelArr,0.6,0.001,40)
b,alphas = smo.smoP(dataArr,labelArr,0.01,0.001,100)

ws = smo.calcWs(alphas,dataArr,labelArr)


print ws
print b

# print type(mat(dataArr))
# print type(labelArr)
# if(len(alphas)>0):
# 		for i in range(100):
# 			   if(alphas[i]>0):
# 			   	print dataArr[i],labelArr[i];
# 			   	ax.scatter(dataArr[i][0],dataArr[i][1],s=100,c = 'r',marker = 'o');
# plt.show()
#fXk = float(multiply(oS.alphas,oS.labelMat).T*(oS.X*oS.X[k,:].T)) + oS.b
fig = plt.figure()
ax = fig.add_subplot(111)
j=0;m=0;n=0;
for i in range(100):	     
				x = dataArr[i][0]
				y = mat(dataArr)[i]*mat(ws)+b
				if(alphas[i]==0):
											  j=j+1
				if(alphas[i]>0):
					              ax.scatter(dataArr[i][0],dataArr[i][1],s=100,c = 'r',marker = 'o') 
 			  			          #print dataArr[i],labelArr[i]
 			 
				#print ('x=%f,y=%f' % (x,y))
				#ax.plot(int(x),int(y))
				#ax.scatter(int(x),int(y),s=100,c = 'r',marker = 'o')       
				
				if((y>0) and (alphas[i]==0)):
						 m=m+1;ax.scatter(dataArr[i][0],dataArr[i][1],s=50,c = 'b',marker = '*')          
				elif((y<0) and (alphas[i]==0)) :
						 n=n+1;ax.scatter(dataArr[i][0],dataArr[i][1],s=50,c = 'g',marker = 's')
			  
print j;
print m;
print n;
plt.show()

