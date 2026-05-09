import numpy as np

a1 = np.array([10, 20, 30])
a2 = np.array([[10, 20, 30], [20, 20, 30]])

print("Сумма:", np.sum(a1), np.sum(a2))
print("Среднее:", np.mean(a1), np.mean(a2))
print("Минимум:", np.min(a1), np.min(a2))
print("Максимум:", np.max(a1), np.max(a2))
print("Поэлементное сложение:", a1 + a1)
print("Поэлементное умножение:", a1 * a1)
print("Умножение на скаляр:", a1 * 2)
print("Прибавление скаляра:", a2 + 5)

flat_a2 = [x for row in a2 for x in row]

print("Сумма:", sum(a1), sum(flat_a2))
print("Среднее:", sum(a1) / len(a1), sum(flat_a2) / len(flat_a2))
print("Минимум:", min(a1), min(flat_a2))
print("Максимум:", max(a1), max(flat_a2))
print("Поэлементное сложение a1 + a1:", [x + x for x in a1])
print("Умножение на скаляр:", [x * 3 for x in a1])