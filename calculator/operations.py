import math


# здесь математические операции
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Ошибка: деление на ноль")
    return a / b


def remainder(a, b):
    if b == 0:
        raise ValueError("Ошибка: деление на ноль")
    return a % b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Ошибка: корень из отрицательного")
    return math.sqrt(a)


def sin_func(x):
    return math.sin(x)


def cos_func(x):
    return math.cos(x)


def floor_func(x):
    return math.floor(x)


def ceil_func(x):
    return math.ceil(x)


# для удобного импорта в тестах
__all__ = ['add', 'subtract', 'multiply', 'divide', 'remainder',
           'power', 'square_root', 'sin_func', 'cos_func',
           'floor_func', 'ceil_func']
