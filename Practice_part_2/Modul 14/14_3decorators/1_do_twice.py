# Задача 1. Двойной вызов
# Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию.
# Не забывайте про документацию и аннотации типов.

# Пример декорируемой функции:
#
# def greeting(name):
#
#     print('Привет, {name}!'.format(name=name))
#
#
#
# Основной код:
#
# greeting('Tom')
#
#
#
# Результат:
#
# Привет, Tom!
#
# Привет, Tom!

from typing import Callable, Any


def teh_kah(func: Callable) -> Callable:
    """Декоратор, вызывающий функцию дважды"""

    def wrapped_greeting(*args, **kwargs) -> Any:
        for _ in range(2):
            func(*args, **kwargs)
        return func

    return wrapped_greeting


@teh_kah
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
