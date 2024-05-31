
class Ominaisuus:
    """
    Суперкласс описывающий собственность
    args:
        arvo - стоимость (вводится пользователем)
        kerroin - коэффициент (необходим для метода вычисления налога)
        raha - количество денег (вводится пользователем)

    """
    Title = 'Ominaisuus'

    def __init__(self):
        # введите стоимость {авто}
        self.arvo = int(input('Syötä {}n arvo '.format(self.Title)))
        self.kerroin = 1
        # Сколько у вас денег?
        self.raha = int(input('Paljonko rahaa sinulla on? '))

    def vero(self):
        vero = self.arvo * self.kerroin / 1000
        return vero

    def tarpeeksi(self):
        tarpeeks = self.raha - self.vero()
        if tarpeeks >= 0:
            print('Sinulla on tarpeeksi rahaa')
        else:
            print('Sinulta puutuu {}:n ruplaa'.format(abs(tarpeeks)))

    def __str__(self):
        return '{}n arvo on {}. {}n vero on {}'.format(
            self.Title, self.arvo, self.Title, self.vero()
        )


class Asunto(Ominaisuus):
    """Класс описывающий квартиру"""
    Title = 'Asunto'

    def __init__(self):
        super().__init__()
        self.kerroin = 1


class Auto(Ominaisuus):
    """Класс описывающий автомобиль"""
    Title = 'Auto'

    def __init__(self):
        super().__init__()
        self.kerroin = 5


class Kartano(Ominaisuus):
    """Класс описывающий сельский дом"""
    Title = 'Mökki'

    def __init__(self):
        super().__init__()
        self.kerroin = 2


veron_asunto = Asunto()
veron_asunto.vero()
print(veron_asunto)
veron_asunto.tarpeeksi()

veron_auto = Auto()
veron_auto.vero()
print(veron_auto)
veron_auto.tarpeeksi()

veron_kartano = Kartano()
veron_kartano.vero()
print(veron_kartano)
veron_kartano.tarpeeksi()
