# Задача 3. Корень диска
# Напишите программу, которая выводит на экран только корень диска,
# на котором запущен скрипт. Учтите, что скрипт может быть запущен
# где угодно и при любой вложенности папок.
#
#
#
# Результат программы на примере диска G:
#
# Корень диска: G:\\
import os

cwd = os.getcwd()
print('Current working directory: {0}'.format(cwd))

path = '/'
dir_list = os.listdir(path)

# Print the list
print(dir_list)
print("Корень диска:", os.path.abspath(os.sep).split(os.sep)[0])
