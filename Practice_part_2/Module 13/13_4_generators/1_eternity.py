# Задача 1. Бесконечный генератор
# По аналогии с бесконечным итератором из практики предыдущего урока,
# реализуйте свой счётчик-генератор, который также в цикле будет бесконечно выдавать значения.
#
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.
def count_iterator():
    laskuri = 0
    while True:
        laskuri += 1
        yield laskuri
def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


my_gener = count_iterator()

for i in get_prime_numbers(50):
    print(i, end='\t')
print()

