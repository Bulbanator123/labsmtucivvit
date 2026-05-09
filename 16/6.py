import numpy as np

a1 = np.array([15, 3, 27, 8, 19])
a2 = [15, 3, 27, 8, 19]

print("Отсортированный массив:", np.sort(a1), sorted(a2))
print("Индекс максимального элемента:", np.argmax(a1), a2.index(max(a2)))
