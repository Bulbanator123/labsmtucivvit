def greet(name: str) -> None:
    # Напишите тело функции
    print("Привет, {}!".format(name))


def square(number):
    # Напишите тело функции
    return number * number


def max_of_two(x, y):
    # Напишите тело функции
    return max(x, y)


greet("mtuci")
greet("Мир")
greet("Даниил")

print(square(4))
print(square(-1))
print(square(1.5))

print(max_of_two(5, 2))
# т.к вещественные числа могут записываться с погрешностью в компьютере
# то может быть неточный вывод функции
print(max_of_two(5.0, 5.0))
print(max_of_two(2, 3))

# Ошибки

# greet("1", "2")  # функция принимает только 1 аргумент

# print(square("aerajae"))  # функция работает корректно только с int или float
# print(square(10, 10))  # функция принимает только 1 аргумент

# print(max_of_two(10))  # функция принимает только 1 аргумент
# print(max_of_two("afjafj"))  # функция работает корректно только числа
