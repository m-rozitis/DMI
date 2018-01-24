import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-4, 4, 0.01)

y = (1+(x))*np.exp(x)
plt.plot(x, y)

def my_function(x):
    k = 0
    a = 1*(k+1)
    S = a
    while k < 500:
        k = k + 1
        R = ((k+1)*x)/(k*k)
        a = a * R
        S = S + a
    return S

yy = my_function(x)
plt.plot(x, yy, 'g')
plt.grid(color='green')
plt.show()
