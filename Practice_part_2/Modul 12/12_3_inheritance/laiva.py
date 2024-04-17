
class Laiva:

    def __init__(self, malli):
        self.__malli = malli

    def __str__(self):
        return '\nLaivan malli on {malli}'.format(
            malli=self.__malli
        )

    def meno(self):
        print('Laiva on lähtenyt')


class Rahtilaiva(Laiva):
    """Класс Грузовой корабль
        Args:
            malli - модель корабля, передается из суперкласса
            self.rahti - передается загруженность корабля
        """

    def __init__(self, malli):
        super().__init__(malli)
        self.rahti = 0

    def lastaus(self):
        """Метод погрузка для погрузки"""
        # Погружаем груз на корабль
        print('Lastataan lastia laivaan')
        self.rahti += 1

    def lossaus(self):
        """Метод разгрузка для разгрузки"""
        # Разгружаем корабль
        print('Purataan laivaa')
        if self.rahti > 0:
            self.rahti -= 1
        else:
            print('Laiva on jo purattu!')


class Sotalaiva(Laiva):
    """Класс Военный корабль
    Args:
        malli - модель корабля, передается из суперкласса
        aseisitus - передается вооружение корабля
    """

    def __init__(self, malli, aseisitus):
        super().__init__(malli)
        self.aseistus = aseisitus

    def attack(self):
        # Военный корабль атакует оружием:
        print('Sotolaiva hyökkää aseilla: {}'.format(self.aseistus))


laiva_1 = Sotalaiva(malli='zxc3', aseisitus='tykki')
laiva_2 = Rahtilaiva('Eskerö')
laiva_2.lastaus()
laiva_2.lossaus()
laiva_1.attack()
