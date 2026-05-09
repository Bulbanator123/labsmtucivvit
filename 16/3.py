import numpy as np

a = np.array([[10, 20, 30],
              [20, 20, 30]])

print("Сумма по строкам:", np.sum(a, axis=1))
print("Сумма по столбцам:", np.sum(a, axis=0))

print("Среднее по строкам:", np.mean(a, axis=1))
print("Среднее по столбцам:", np.mean(a, axis=0))

print("Минимум по столбцам:", np.min(a, axis=1))
print("Максимум по столбцам:", np.max(a, axis=0))

print("Сумма по строкам:", [sum(row) for row in a])

col_sums = []
num_cols = len(a[0])
for j in range(num_cols):
    col_sums.append(sum([a[i][j] for i in range(len(a))]))

print("Сумма по столбцам:", col_sums)