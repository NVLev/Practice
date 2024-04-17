class Ship:

    def __init__(self, model="корабль"):
        self.model = model

    def __str__(self):
        return self.model

    def sail(self):
        print(f"{self.model} идёт по воде!")


class WarShip(Ship):

    def __init__(self, weapon, model="военный корабль"):
        super().__init__(model)
        self.weapon = weapon

    def attack(self):
        print(f"{self} делает пиу-пиу!")


class CargoShip(Ship):

    def __init__(self, model="грузовой корабль"):
        super().__init__(model)
        self.fullness = 0

    def loading(self, value):
        self.fullness += value

    def unloading(self, value):
        self.fullness -= value

