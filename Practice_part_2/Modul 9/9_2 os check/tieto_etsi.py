# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла,
# проходит по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.
# Пример:
#
# Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
#
# Имя файла: lesson2
# Найдены следующие пути:
#
# C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
#
# C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
#
# C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
#
# C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py
#
# C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py
#
# C:/Users/Roman/PycharmProjects/Skillbox\Module20\lesson2.py
#
# C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py
#
# C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py

import os

def tieto_etsi(polku, tieto_nimi):
    for i_kansio in os.listdir(polku):
        polku = os.path.join(polku, i_kansio)
        if tieto_nimi == i_kansio:
            print(os.path.abspath(polku))
        elif os.path.isdir(polku):
            tulos = tieto_etsi(polku, tieto_nimi)



tieto_etsi('..', 'main1.py')


