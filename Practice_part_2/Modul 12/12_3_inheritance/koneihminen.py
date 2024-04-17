class Koheihminen:
    """Суперкласс Роботы"""
    def __init__(self, numero):
        self.numero = numero

class Imurin(Koheihminen):
    """Класс, описывающий робота-пылесоса,
    наследует от Робота
    """
    def __init__(self, numero, roskapussi=0):
        super().__init__(numero)
        self.roskapussi = roskapussi

    def toimi(self):
        print('Olen imuroimassa, minun roskapussi on', self.roskapussi)


class Sotilas(Koheihminen):
    """Класс, описывающий робота-воина
        наследует от Робота"""
    def __init__(self, numero, aseisitus):
        super().__init__(numero)
        self.aseistus = aseisitus

    def toimi(self):
        print('Suojelen kohdetta {}malla'.format(self.aseistus))


class Sukellusvene(Sotilas):
    """Класс, описывающий подводную лодку
    наследует от Робота"""
    def __init__(self, numero, aseisitus, syva):
        super().__init__(numero, aseisitus)
        self.syva = syva

    def toimi(self):
        print('Suojelen kohdetta {}malla. Syvä on {}'.format(self.aseistus, self.syva))

bob = Imurin()