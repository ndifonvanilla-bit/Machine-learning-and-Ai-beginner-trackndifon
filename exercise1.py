import numpy as np
linpace_array = np.linspace(0, 1, 20)
identity = np.eye(5)
rand_ints = np.random.randint(1, 101, size=(3, 4))

print("linspace -> shape:", linspace.shape, "dtype", linspace.dtype)
print("identity -> shape:", identity.shape, "dtype:", identity.dtype)
print("rand_ints -> shape:", rand_ints.shape, "dtype:", rand_ints.dtype)
