import numpy as np

def serie(n, x):
    a = 0
    m = 5*x
    for i in range(0, n):
        a += (np.cos(m))
        
    return a

def table(z):
    b = []
    c = 0.157079633
    for i in range(0, 20):
        b.append(serie(z, i*c*(np.pi)))
        
    for i in range(0, 20):
        print(b[i])
        
table(1)