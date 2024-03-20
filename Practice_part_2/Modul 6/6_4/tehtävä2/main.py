
import random


def pop(set1):
    a = min(set1)
    print('pienin', a)
    set1.remove(a)
    return set1


nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26,
          3, 11, 2, 3, 16, 19, 21,
          2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]

nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5,
          19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15,
          16, 9, 1, 13, 21, 21]
# реобразует списки во множества и убирает повторяющиеся элементы.
# Затем удаляет минимальный элемент из каждого множества и добавляет
# туда случайное число в диапазоне от 100 до 200. Затем выполните
# следующие действия со множествами:

nums_1 = set(nums_1)
print('Ensimmäinen joukko', nums_1)
nums_2 = set(nums_2)
print('Toisen joukko', nums_2)
nums_1_uusi = pop(nums_1)
print(nums_1_uusi)
nums_2_uusi = pop(nums_2)
print(nums_2_uusi)

nums_1_uusi.add(random.randint(100, 200))
print(nums_1_uusi)
nums_2_uusi.add(random.randint(100, 200))
print(nums_2_uusi)

# Вывести все элементы множеств (объединение).
# Вывести только общие элементы (пересечение).
# Вывести элементы, входящие в nums_2, но не входящие в nums_1.

print('yhdistäminen', nums_1_uusi | nums_2_uusi)
print(nums_1_uusi & nums_2_uusi)
print(nums_2_uusi - nums_1_uusi)
