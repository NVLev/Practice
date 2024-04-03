# Напишите программу, которая копирует код каждого скрипта в папке проекта
# python_basic в файл scripts.txt, разделяя код строкой из 40 символов *.
#
#
#
# Пример содержимого файла scripts.txt:
#
# import platform
#
# import sys
#
#
#
# info = 'OS info is \n{}\n\nPython version is {} {}'.format(
#
#     platform.uname(),
#
#     sys.version,
#
#     platform.architecture(),
#
# )
#
# print(info)
#
#
#
# with open('os_info.txt', 'w', encoding='utf8') as file:
#
#     file.write(info)
#
# ****************************************
#
# print("Введите первую точку")
#
# x1 = float(input('X: '))
#
# y1 = float(input('Y: '))
#
# print("\nВведите вторую точку")
#
# x2 = float(input('X: '))
#
# y2 = float(input('Y: '))
#
#
#
# print("Уравнение прямой, проходящей через эти точки:")
#
# x_diff = x1 - x2
#
# y_diff = y1 - y2
#
# if x_diff == 0:
#
#     print("x = ", x1)
#
# elif y_diff == 0:
#
#     print("y = ", y1)
#
# else:
#
#     k = y_diff / x_diff
#
#     b = y2 - k * x2
#
#     print("y = ", k, " * x + ", b)

import os

cwd = os.getcwd()
print('Kansio', cwd)
os.chdir('../')
print('Kansio', cwd)



def find_file(cur_path, ending):
    all_paths = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if i_elem.endswith(ending):
            all_paths.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, ending)
            if result:
                all_paths.extend(result)

    return all_paths


def get_text_from_file(path_to_file):
    file = open(path_to_file, "r", encoding="utf8")
    result = ""
    for line in file:
        result += line
    return result


all_py_files = find_file('C:\\Users\\natal\\PycharmProjects\\Python_Basic', '.py')


file_result = open("scripts.txt", "w", encoding="utf8")

for file_path in all_py_files:
    file_result.write(get_text_from_file(file_path))
    file_result.write("\n" * 2 + "*" * 80 + "\n" * 2)
file_result.close()
