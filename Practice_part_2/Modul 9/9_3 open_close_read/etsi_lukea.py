# Используя функцию поиска файла из предыдущего урока, реализуйте программу,
# которая находит внутри указанного пути все файлы с искомым названием и
# выводит на экран текст одного из них (выбор можно сгенерировать случайно).
#
# Подсказка: можно использовать, например, список для сохранения найденного пути.
import os
import random


def tieto_etsi(polku, tieto_nimi):
    print(polku)
    koko_polku = []
    for i_kansio in os.listdir(polku):
        polku = os.path.join(polku, i_kansio)
        print(polku)
        if i_kansio in tieto_nimi:
            koko_polku.append(os.path.abspath(polku))
        elif os.path.isdir(polku):
            tulos = tieto_etsi(polku, tieto_nimi)
            if tulos:
                koko_polku.extend(tulos)

    return koko_polku


def check_file_inside(path_to_file):
    file = open(path_to_file, "r", encoding="utf8")
    for line in file:
        print(line)
    file.close()


all_paths = tieto_etsi(
    "..",
    (
        "main1.py",
        "main2.py",
        "main3.py",
    ),
)

print(all_paths)
# check_file_inside(random.choice(all_paths))
