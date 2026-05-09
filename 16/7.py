import time
import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype=np.int64)
b = a.astype(np.float64)

print(a.dtype, b.dtype)
print(a.nbytes, b.nbytes)

a = np.array([1, 2, 3], dtype=np.int32)
b = np.array([1, 2, 3], dtype=np.float64)
print(a / 3, b / 3)
# ---------------------------------------------------
n = 10000000
a = np.ones(n)

start1 = time.time()
np.sum(a)
time1 = time.time() - start1
a = [1] * n

start2 = time.time()
sum(a)
time2 = time.time() - start2

print("NumPy время:", time1)
print("Python время:", time2)