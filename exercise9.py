import numpy as np
w = np.random.randn(4, 3)
x = np.random.randn(3, 10)
z = w @ x
b = np. random.randn(4, 1)

print("w shape:", w.shape)
print("x shape:", x.shape)
print("z shape:", z.shape)
print("z+b shape:", z+b.shape)
