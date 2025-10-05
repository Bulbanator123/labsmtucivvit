# импорты
from math import sqrt

# Модуль


def summa(num1: int, num2: int) -> int:
    # сумма двух эментов
    return num1 + num2


def subst(num1: int, num2: int) -> int:
    # разность двух эментов
    return num1 - num2


def multi(num1: int, num2: int) -> int:
    # произведение двух эментов
    if num2 == 0:
        raise ValueError("Деление на ноль невозможно")
    return num1 * num2


def devide(num1: int, num2: int) -> int:
    # частное (целое) двух эментов
    return num1 // num2


def Pifagor(num1: int, num2: int) -> float:
    # теорема пифагора
    return sqrt(num1 * num1 + num2 * num2)
