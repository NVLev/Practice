# Задача 1. Функции
# Дана функция func_1, которая принимает число и возвращает результат его сложения с числом 10:
#
#
#
# def func_1(x):
#
#     return x + 10
#
#
#
# Реализуйте функцию высшего порядка func_2, которая будет возвращать перемножение двух
# результатов переданной функции.
#
# Пример основного кода:
#
# print(func_2(func_1, 9))
#
#
#
# Результат: 361.
from typing import Any
def func_2(func, *args, **kwargs) -> Any:
    tulos = func(*args, **kwargs)
    laskuri = 0
    tulos *= tulos

    return tulos



def func_1(x) -> int:

    return x + 10



print(func_2(func_1, 9))