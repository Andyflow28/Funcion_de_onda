import numpy as np
import matplotlib.pyplot as plt

def serie(n, x):
    a = 0
    lamda = np.pi
    amplit = 0
    for i in range(0, n):
        lamda += (np.pi/n)
        amplit += 1/n
        a += amplit*(np.cos(2*np.pi*(x/lamda)))
        
    return a

x = np.arange(-(10*np.pi),10*(np.pi),np.pi/1000)
y = serie(5000000, x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('Phi(x)')
plt.title('Funcion de Onda')
plt.show()