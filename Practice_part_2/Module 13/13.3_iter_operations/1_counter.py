# Задача 1. Бесконечный итератор
# Реализуйте итератор-счётчик, который не принимает никаких атрибутов и имеет
# только один статический атрибут — счётчик. Итератор увеличивает счётчик и
# возвращает предыдущее значение. У вас должен получиться бесконечный итератор.
#
# То есть при вызове такого кода в основной программе
#
# my_iter = СountIterator()
#
# for i_elem in my_iter:
#
#     print(i_elem)
#
# значения будут выдаваться бесконечно.
import random
class СountIterator:
    laskuri = 0

    def __iter__(self):
        return self

    def __next__(self):
        СountIterator.laskuri += 1

        return СountIterator.laskuri

my_iter = СountIterator()

for i_elem in my_iter:
    print(i_elem)