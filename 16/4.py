import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

print(a + 10)
print(a + b)

a = [[1, 2, 3],
     [4, 5, 6]]

b = [10, 20, 30]
print([[x + 10 for x in row] for row in a])
a = [[a[0][i] + b[i] for i in range(len(b))], a[1]]
print(a)
