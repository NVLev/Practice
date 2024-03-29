#Задача 2. Содержимое
# Выберите любую директорию на своём диске и затем напишите программу, выводящую на экран абсолютные пути к файлам и папкам,
# которые находятся внутри этой директории.
#
#
#
# Результат программы на примере директории проекта python_basic:
#
# Содержимое каталога G:\PycharmProjects\python_basic
#
#     G:\PycharmProjects\python_basic\.git
#
#     G:\PycharmProjects\python_basic\.idea
#
#     G:\PycharmProjects\python_basic\Module14
#
#     G:\PycharmProjects\python_basic\Module15
#
#     G:\PycharmProjects\python_basic\Module16
#
#     G:\PycharmProjects\python_basic\Module17
#
#     G:\PycharmProjects\python_basic\Module18
#
#     G:\PycharmProjects\python_basic\Module19
#
#     G:\PycharmProjects\python_basic\Module20
#
#     G:\PycharmProjects\python_basic\Module21
#
#     G:\PycharmProjects\python_basic\Module22
import os

def tulos_dirs(suun):
    print('\n Kansion sisään', suun)
    for i_piste in os.listdir(suun):
        polku = os.path.join(suun, i_piste)
        print('      ', polku)

sunni_lista = ['PycharmProjects']
for i_suun in sunni_lista:
    tietopolku = os.path.abspath(os.path.join('..','..', i_suun))
    tulos_dirs(tietopolku)