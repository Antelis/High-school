import numpy as np

x = np.array([1, 5, 8, 3, 30, 9, 13])

for xi in x:
    #print(xi)
    if xi > 3 and xi % 2 != 0:
        print(xi)