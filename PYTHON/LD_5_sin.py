import random
import numpy as np
import matplotlib.pyplot as plt

def mans_sinuss(x):
    y = np.sin(x)
    return y

N = 100000
x = []
y = []
a = -np.pi/2
b = np.pi/2
c = -1
d = 1

for i in range(N):
    x.append(random.uniform(a,b))
for i in range(N):
    y.append(random.uniform(c,d))

red_x = []
red_y = []
green_x = []
green_y = []

for i in range(N):
    if (y[i] < mans_sinuss(x[i]) and y[i] > 0) \
    or (y[i] > mans_sinuss(x[i]) and y[i] < 0):
        green_x.append(x[i])
        green_y.append(y[i])
    else:
        red_x.append(x[i])
        red_y.append(y[i])

plt.plot(green_x,green_y,'go')
plt.plot(red_x,red_y,'rv')
plt.grid()
plt.show()

areaRect = (b-a)*(d-c)
areaSin = areaRect * len(green_x) / N
print areaSin
