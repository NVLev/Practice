# Задача 2. Непонятно!
# Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами и их id.
# Видя, как он мучается, вы решили помочь ему и объяснить эту тему наглядно.
#
# Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных,
# информацию о его изменяемости, а также id этого объекта.
#
# Помните, что через input можно получить только строку, что бы вы ни вводили.
# В данном случае ввод можно выполнить вручную, просто вписав нужный объект в переменную,
# без использования функции input.

# Пример 1:
#
# Введите данные: привет
#
#
#
# Тип данных: str (строка)
#
# Неизменяемый (immutable)
#
# Id объекта: 1705156583984
#
#
#
# Пример 2:
#
# Введите данные: {‘a’: 10, ‘b’: 20}

# Тип данных: dict (словарь)
#
# Изменяемый (mutable)
#
# Id объекта: 1705205308536

def kuva(tieto):
    if isinstance(tieto, str):
        print('Tietotyyppi: str')
        print('Muuttumaton (immutable)')
        print('Objektin tunnus', id(tieto))
    elif isinstance(tieto, dict):
        print('Tietotyyppi: dict')
        print('Muuttuva (mutable)')
        print('Objektin tunnus', id(tieto))
    elif isinstance(tieto, list):
        print('Tietotyyppi: lista')
        print('Muuttuva (mutable)')
        print('Objektin tunnus', id(tieto))
    elif isinstance(tieto, tuple):
        print('Tietotyyppi: monikko (tuple)')
        print('Muuttumaton (immutable)')
        print('Objektin tunnus', id(tieto))
    elif isinstance(tieto, set):
        print('Tietotyyppi: joukko (set)')
        print('Muuttuva (mutable)')
        print('Objektin tunnus', id(tieto))
    elif isinstance(tieto, int):
        print('Tietotyyppi: numero (int)')
        print('Muuttumaton (immutable)')
        print('Objektin tunnus', id(tieto))


minun_tieto = 'привет'
print(kuva(minun_tieto))

