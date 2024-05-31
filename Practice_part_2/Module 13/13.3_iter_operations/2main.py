# Каждый новый элемент — это сумма случайного вещественного числа
# от 0 до 1 и предыдущего элемента
# (первый элемент — просто случайное вещественное число от 0 до 1)
import random
class SatunNumero:
    def __init__(self, num):
        self.laskuri = 0
        self.ens_num = random.uniform(0,1)
        self.num = num + 1

    def __iter__(self):
        self.laskuri = 0
        self.ens_num = random.uniform(0, 1)

        return self

    def __next__(self):
        print(self.ens_num)
        self.laskuri += 1
        if self.laskuri > 1:
            if self.laskuri > self.num:
                raise StopIteration()
            self.kaks_num = round(self.ens_num + random.uniform(0, 1), 2)
            return self.kaks_num


sat_iterator = SatunNumero(6)
for i_num in sat_iterator:
    print(i_num)
