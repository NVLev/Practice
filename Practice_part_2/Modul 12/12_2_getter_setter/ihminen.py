# инициализируется именем (имя должно состоять только из букв) и возрастом
# (должен быть в диапазоне от 0 до 100), а
# внутри класса считается общее количество инициализированных объектов.

class Ihminen:
    count = 0

    def __init__(self, nimi, vuosi):
        self.__nimi = nimi
        self.__vuosi = vuosi
        self.set_nimi(nimi)
        self.set_vuosi(vuosi)
        Ihminen.count += 1

    def get_nimi(self):
        return self.__nimi

    def get_vuosi(self):
        return self.__vuosi

    def set_nimi(self, nimi):
        if isinstance(nimi, str):
            self.__nimi = nimi
        else:
            raise Exception('Nimi ei ole sano')

    def set_vuosi(self, vuosi):
        if vuosi in range(0, 101):
            self.__vuosi = vuosi
        else:
            raise Exception('Ikä ei ole numero')

    def __str__(self):
        return 'Ihmisen nimi on: {}, hänen ikä on {}.  Koko ihmisten määrä on {}'.format(
            self.__nimi, self.__vuosi, self.count)


pekko = Ihminen('Pekko', 20)
pirjo = Ihminen('Pirjö', 82)

print(pirjo)
print(pekko)
