# Задача 2. Таймер 2
# Для замера времени передачи различных данных на множество сайтов вы
# написали специальную функцию, которая сделала всю работу за вас,
# что позволило большую часть времени смотреть видео с котиками в интернете.
# Однако, увидев свой код, вы как программист с опытом поняли, что этот код можно
# написать намного красивее и удобнее.
#
# Реализуйте декоратор, который замеряет время работы задекорированной
# функции и выводит ответ на экран. Для проверки примените декоратор к какой-нибудь
# «тяжеловесной» функции и вызовите её в основной программе.
import functools
from functools import wraps
import time
from typing import Callable, Any
import random


def timer_wrapper(func: Callable) -> Callable:
    """
        Декоратор, выводящий время выполнения
        декорируемой функции
        """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        alkaa = time.time()
        tulos = func(*args, **kwargs)
        loppua = time.time()
        aika = round(loppua - alkaa, 4)
        print('Funktion suoritusaika on {}'.format(aika))
        return tulos

    return wrapper


@timer_wrapper
def create_random_tuple(a: int, b: int, n: int) -> tuple:
    """Фукнция, создающая кортеж из рандомных чисел"""
    return tuple([random.randint(a, b) for _ in range(n)])


@timer_wrapper
def hard_func():
    return [x ** 2 ** x for x in range(22)]


create_random_tuple(0, 5, 10)
hard_func()
print(create_random_tuple.__doc__)
print(hard_func.__name__)

