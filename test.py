__author__ = 'Sebastian Sanchez Perez-Moreno. Email: s.sanchezperezmoreno@tudelft.nl'
from time import time
x = []
start = time()
for _ in range(100):
    x.append(0)
stop = time()
print(stop - start)
for _ in range(0, 100, 10):
    x.append(0)
    x.append(0)
    x.append(0)
    x.append(0)
    x.append(0)
    x.append(0)
    x.append(0)
    x.append(0)
    x.append(0)
    x.append(0)
print(time() - stop)