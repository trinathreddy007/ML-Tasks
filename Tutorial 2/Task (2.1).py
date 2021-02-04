In [1]:
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
x = np.array([1,2,3])
y = np.array([1.2,1.9,3.2])
size = len(x)
sum_xy = np.dot(x,np.transpose(y))
sum_x = x.sum()
sum_y = y.sum()
sum_xxt = np.dot(x,np.transpose(x))
w1 = ((size*sum_xy)-(sum_x*sum_y))/((size*sum_xxt)-(sum_x**2))
w0 = ((sum_y*sum_xxt)-(sum_xy*sum_x))/((size*sum_xxt)-(sum_x**2))
y_hat = []
for i in range(0,size):
    temp = w0 + w1*x[i]
    y_hat.append(temp)
y_hat = np.array(y_hat)
sns.lineplot(x,y_hat)
sns.scatterplot(x,y,color='pink')
In [ ]:

In [ ]:
