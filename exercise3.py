import numpy as np
mat = np.rand(6,6)
print("original matrix:\n", mat)

rows = mat[::2]
print("\nEvery other row:\n", rows)

diag = np.diag(mat)
print("\nDiagonal:\n", diag)

binary = (mat > 0.7).astype(int)
print("\nBinary matrix:\n", binary)