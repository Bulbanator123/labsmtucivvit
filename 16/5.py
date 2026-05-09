import numpy as np

a1 = np.array([5, 13, 7])
a = np.array([5, 12, 7, 20, 3, 15])
b = np.array([[5, 12, 7], [20, 13, 15]])
print(a[a > 10])
print(b[b > 10])
print(a1 == b)
print([x for x in a if x > 10])
print([x for row in b for x in row if x > 10])
