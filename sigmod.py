import numpy as np
import matplotlib.pyplot as plt
#help(plt)
# y = 1/(1+(np.e)**(-x))
x = np.arange(-5, 5, 0.1);
y = 1/(1+(np.e)**(-x))
plt.plot(x, y)
plt.scatter(0,0.5,s=100,c = 'r',marker = 'o')  
plt.annotate('(0,0.5)', xytext=(0.2, 0.5),xy=(0,0.5))
plt.show()