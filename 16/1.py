import numpy as np

a1 = np.array([10, 20, 30])

a2 = np.array([[10, 20, 30], [20, 20, 30]])

print(a1.ndim) # размерность массива
print(a1.shape) # форма массива
print(a1.dtype) # тип данных

print(a2.ndim) # размерность массива
print(a2.shape) # форма массива
print(a2.dtype) # тип данных

print(np.std(a1))
print(np.std(a2))
print(a2[1, 1])
print(a2[1, :])
print(a2[:, 1])
print(a2[:, 1:2])

print(a1 == a2)