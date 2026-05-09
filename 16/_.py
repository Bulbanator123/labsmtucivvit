import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3],
[4, 5, 6]])
print(a.ndim) # размерность массива
print(a.shape) # форма массива
print(a.dtype) # тип данных

print(np.sum(a))
print(np.mean(a))
print(np.min(a), np.max(a))
print(np.std(a))

print(np.sum(b, axis=0)) # сумма по столбцам
print(np.sum(b, axis=1)) # сумма по строкам

print(a + 10)
print(b * 2)
c = np.array([10, 20, 30])
print(b + c)

mask = a > 3
print(mask)
print(a[mask])