import numpy as np
arr = np.arange(1, 25)
print("\noriginal:", arr.shape)
arr_3d = arr.reshape(2, 3, 4)
print("3-D", arr_3d.shape)
arr_2d = arr_3d.reshape(6, 4)
print("2-D:", arr_2d.shape)
flattened = arr_2d.flatten()
print("flattened:", flattened.shape)