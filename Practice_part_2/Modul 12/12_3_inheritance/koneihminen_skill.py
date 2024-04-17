class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class WarRobot(Robot):

    def __init__(self, gun, model):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print(f'Робот охраняет военный обьект при помощи {self.gun}')


class VacuumCleaningRobot(Robot):

    def __init__(self, model):
        super().__init__(model)
        self.garbage_bag = 0

    def operate(self):
        print('Робот пылесосит пол')


class SubmarineRobot(WarRobot):

    def __init__(self, gun, model, depth):
        super().__init__(gun, model)
        self.depth = depth

    def operate(self):
        super().operate()
        print('Охрана ведется под водой на глубине', self.depth)
