import numpy as np
col = np.arange(4).reshape(4, 1)
row = np.arange(5).reshape(1, 5)
result1 = col + row
print("(4, 1) + (1, 5) -> shape:", result1.shape)
matrix = np.arrange(12).reshape(4, 3)
vec = np.array([1, 2, 3])
result2 = matrix + vec
print("(4, 3) + (3) -> shape:", result2.shape)