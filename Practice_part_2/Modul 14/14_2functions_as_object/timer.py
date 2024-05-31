# С помощью понятия функции высшего порядка реализуйте функцию-таймер, которая замеряет время работы переданной функции func и выдаёт ответ на экран.
#
# Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.

import time
from typing import Callable, Any

def timer(func, *args, **kwargs) -> Any:
    """Функция таймер"""
    alkaa = time.time()
    tulos = func(*args, **kwargs)
    loppua = time.time()
    aika = round(loppua - alkaa, 4)
    return tulos
