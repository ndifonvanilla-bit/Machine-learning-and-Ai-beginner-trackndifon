import numpy as np
x = np.random.rand(100, 5)
col_min = np.min(x, axis=0)
col_max = np.max(x, axis=0)
x_scaled = (x - col_min) / ( - col_min)

print("min per column:", x_scaled.min(axis=0))
print("max per column:", x_scaled.max(axis=0))
