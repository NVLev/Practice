# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке. Напишите программу, которая выводит их сумму в выходной файл answer.txt.
#
#
#
# Пример:
#
# Содержимое файла numbers.txt:
#
# 1
#
# 2
#
# 3
#
# 4
#
# 10
#
#
#
# Содержимое файла answer.txt
#
# 20

num_tieto = open('numbers.txt', 'r', encoding='utf-8')
summa_lista = [int(i_num) for i_num in num_tieto if i_num != '\n']
num_tieto.close()
summa = sum(summa_lista)
summa_tieto = open('summa_tieto.txt', 'w')
summa_tieto.write(str(summa))
summa_tieto.close()
summa_tieto = open('summa_tieto.txt', 'r')
for i in summa_tieto:
    print(i)
summa_tieto.close()
