import numpy as np
x = np.random.randn(100, 5)
mean = np.mean(x, axis=0)
std = np.std(x, axis=0)
z = (x - mean) / std

print("column means:", np.mean(z, axis=0))
print("column std :", np.std(z, axis=0))

