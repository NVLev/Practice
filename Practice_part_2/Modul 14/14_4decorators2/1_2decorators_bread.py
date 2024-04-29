# Есть функция, которая выводит начинку сэндвича.
# Сверху и снизу от начинки идут различные ингредиенты вроде салата,
# помидоров и других. Всё это в свою очередь содержится между двух половинок булочки.
# Реализуйте такую функцию и два соответствующих декоратора — ингредиенты и хлеб.
#
# Пример результата работы программы при вызове функции sandwich:
#
# </----------\>
#
# #помидоры#
#
# --ветчина--
#
# ~салат~
#
# <\______/>

def ainesosat(func, *args, **kwargs):
    """Декоратор, выводящий ингредиенты"""

    def wrap_ainesosat(*args, **kwargs):
        print("#помидоры#")
        func(*args, **kwargs)
        print("~салат~")

    return wrap_ainesosat


def leip(func, *args, **kwargs):
    """Декортатор, выводящий булочку"""

    def wrap_leip(*args, **kwargs):
        print("</----------\>")
        func(*args, **kwargs)
        print('<\______/>')

    return wrap_leip

@leip
@ainesosat
def t_hampurilaisen(sis):
    print(sis)


t_hampurilaisen("ветчина")
