# encoding: utf-8  
import KNN
from numpy import *
import matplotlib 
import matplotlib.pyplot as plt

zhfont = matplotlib.font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')
# group, labels = KNN.createDataSet()
# print KNN.classify0([0,0],group,labels,3)
# zhfont = matplotlib.font_manager.FontProperties(fname='/Library/Fonts/ukai.ttc')

""" 比较好看的绘制方法 """
#KNN.datingClassTest()
KNN.classifyPerson()
plt.figure(figsize=(8, 5), dpi=80)

matrix,labels = KNN.file2matrix('datingTestSet2.txt')  


normDataSet, ranges, minVals=KNN.autoNorm(matrix)
matrix =normDataSet

fig =plt.figure()
axes =fig.add_subplot(111)

type1_x = []
type1_y = []
type2_x = []
type2_y = []
type3_x = []
type3_y = []

for i in range(len(labels)):
    if labels[i] == 1:  # 不喜欢
        type1_x.append(matrix[i][0])
        type1_y.append(matrix[i][1])

    if labels[i] == 2:  # 魅力一般
        type2_x.append(matrix[i][0])
        type2_y.append(matrix[i][1])

    if labels[i] == 3:  # 极具魅力
        #print i, '：', labels[i], ':', type(labels[i])
        type3_x.append(matrix[i][0])
        type3_y.append(matrix[i][1])

type1 = axes.scatter(type1_x, type1_y, s=20, c='red')
type2 = axes.scatter(type2_x, type2_y, s=40, c='green')
type3 = axes.scatter(type3_x, type3_y, s=50, c='blue')
# plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(labels),
#             c=50 * numpy.array(labels), marker='o',
#             label='test')
plt.xlabel(u'每年获取的飞行里程数', fontproperties=zhfont)
plt.ylabel(u'玩视频游戏所消耗的事件百分比', fontproperties=zhfont)
axes.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc=2, prop=zhfont)

plt.show()