# Содержимое файла group_1.txt
#
# Бобровский Игорь 10
#
# Дронов Александр 20
#
# Жуков Виктор 30
#
#
#
# Содержимое файла group_2.txt
#
# Павленко Геннадий 20
#
# Щербаков Владимир 35
#
# Marley Bob 15


file = open('C:\\task\\group_1.txt', 'r', encoding='utf-8')

summa = 0
diff = 0
for i, i_line in enumerate(file):
    if i % 2 == 0:
        info = i_line.split()
        print(info)
        summa += int(info[2])  # Convert info[2] to an integer
        diff -= int(info[2])
file.close()


file_3 = open('C:\\task\\Additional_info\\group_2.txt', 'r', encoding='utf-8')

compose = 1  # Change to 1 for multiplication

for i, i_line in enumerate(file_3):
    if i % 2 == 0:
        info = i_line.split()
        print(info)
        compose *= int(info[2])  # Convert info[2] to an integer

file_3.close()
print(summa)
print(diff)
print(compose)
