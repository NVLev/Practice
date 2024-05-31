from typing import Callable

PLUGINS = dict()


def kirjoita(func: Callable) -> Callable:
    """Декоратор, регистрирует функции как плагины"""
    PLUGINS[func.__name__] = func
    return func


@kirjoita
def sanoo(name: str) -> str:
    return 'Hey, {nimi}'.format(nimi=name)


@kirjoita
def sanoo_2(name: str) -> str:
    return 'Hey-hey, {nimi}'.format(nimi=name)


print(PLUGINS)
print(sanoo_2('Pirjö'))
