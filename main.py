import numpy as np
import matplotlib.pyplot as plt

def series(n, x):
    a = 0
    wave_lenght = np.pi
    amplitude = 0
    for i in range(0, n):
        wave_lenght += (np.pi/n)
        amplitude += 1/n
        a += amplitude*(np.cos(2*np.pi*(x/wave_lenght)))
        
    return a

def graph(n_1, n_2):
    x = np.arange(-(30*np.pi),30*(np.pi),np.pi/n_1)
    y = series(n_2, x)

    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('Phi(x)')
    plt.title('Funcion de Onda (sumatoria de 10 mil funciones de onda)')
    plt.show()


n_0 = 10
n_1 = 1000
n_2 = n_0*n_1

graph(n_1, n_2)


