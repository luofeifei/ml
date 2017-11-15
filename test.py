# coding = utf-8 
from scipy import optimize 
import matplotlib.pyplot as plt  
import numpy as np
from sympy import *
numSteps =0.1
for j in range(-1,int(numSteps)+1):
  print j
# flag=True
# while flag:
# 						inputValue=input("please input a int data :")
						
# 						if(type(inputValue)!=type(1)):
# 							print (inputValue)
# 							raise ValueError
# 						else:
								  
# 							    print inputValue
# 							    flag = False;
# x= Symbol('x');

# y= Symbol('y');


# pprint (cos(x).series(x, 0, 10))
# pprint (diff(sin(2*x), x, 2))
# pprint (diff(tan(x), x))

# pprint (apart(1/( (x+2)*(x+1) ), x))

# print ((x+y)**2).expand()

# #print limit(y,x,0)
# print limit(x,x,oo)
# def f(x):
#   return x**2 + 10 * np.sin(x) 

# x = np.arange(-10, 10, 0.1)

# plt.plot(x, f(x))

# plt.show() 
from sympy.abc import x
from sympy import Integral, latex
# x= Symbol('x')
# y= Symbol('y')

# A = Matrix([[1,x], [y,1]])

# pprint (integrate(6*x**5, x))

# pprint (solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y]))


# print solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])



# print latex(x**2)
# pprint (latex(1/x))
# print latex(Integral(x**2, x))











