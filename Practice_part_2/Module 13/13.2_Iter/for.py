import random
# Задача 1. Свой for (ну почти)
# Дан любой итерируемый объект, например список из N чисел.
# Реализуйте функцию, которая эмулирует работу цикла for с помощью цикла
# while и проходит во всем элементам итерируемого объекта.
# Не забудьте про исключение «конца итерации».
n = int(input("Введите количество чисел: "))
numbers = [random.randint(-100, 100) for _ in range(n)]

buffer_iter = iter(numbers)

while True:
    try:
        print(next(buffer_iter))
    except StopIteration:
        print("Конец!")
        break
