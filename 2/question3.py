def is_prime(number: int) -> bool:
    if type(number) is not int or number < 1:
        print("Это не натуральное число")
        return False
    elif number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


print(is_prime(2))
print(is_prime(10))
print(is_prime(11))
print(is_prime(-1))
print(is_prime(414.42))
print(is_prime("414.42"))  # ????

# ошибки

print(is_prime(414.42, 2))  # функция принимает только 1 аргумент
