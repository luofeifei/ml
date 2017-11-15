# encoding: utf-8  
import numpy as np
import sympy
import matplotlib.pyplot as plt



# x = range(1,7)
# factorial = [np.math.factorial(i) for i in x]
# exponential = [np.e**i for i in x]
# polynomial = [i**3 for i in x]
# logarithmic = [np.log(i) for i in x]

# plt.plot(x,factorial,'black',\
#          x,exponential, 'blue',\
#          x,polynomial, 'green',\
#           x,logarithmic, 'red')

# plt.show()

from sympy.abc import x

print ((x*sympy.ln(1+x))/(x**2)).limit(x,0)

print (  (sympy.sqrt(1+sympy.sin(2*x))-x-1) / (x*sympy.ln(1+x)) ).limit(x,0)

print ((sympy.E**x)/(x**3)).limit(x,sympy.oo)
# result is: oo
print (sympy.ln(x)/x**3).limit(x,sympy.oo)