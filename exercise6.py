import numpy as np
import time 
arr = np.random.rand(1_000_000)

start = time.time()
loop_result = np.array([np.sqrt(x) for x in arr])
loop_time = time.time() - start

start = time. time()
y_vec = np.sqrt()
vec_time = time.time() - start

print("loop time:", loop_time)
print("numpy time:", vec_time)
print("speedup:", loop_time/vec_time)