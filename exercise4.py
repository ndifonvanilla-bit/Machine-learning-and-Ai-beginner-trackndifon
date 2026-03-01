import numpy as np
A = np.random.rand(4, 3)
B = np.randomrand(4, 3)
vstacked = np.vstack((A, B))
hstacked = np.hstack((A, B))
split = np.vsplit(vstacked, 2)

print("vstack ->shape:", vstacked.shape)
print("hstack -> shape:", hstacked.shape)