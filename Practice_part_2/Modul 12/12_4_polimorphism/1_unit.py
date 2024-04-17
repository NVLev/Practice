
# (хитпоинты). У Юнита есть действие «получить урон» (базовый класс получает 0 урона).
#
# Также есть два дочерних класса:
#
# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению.
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма
# (а также инкапсуляции и наследования, конечно же).

class Unit:
    def __init__(self, hitpoints):
        self.hitpoints = hitpoints

    def __str__(self):
        return 'Мои хитпоинты: {}'.format(self.hitpoints)

    def loss(self, numero=0):
        self.hitpoints -= numero
        print('Мой урон - ', self.hitpoints)

class Sotilas(Unit):
    def __init__(self, hitpoints):
        super().__init__(hitpoints)


class Ihminen(Unit):
    def __init__(self, hitpoints):
        super().__init__(hitpoints)

    def loss(self, numero=0):
        self.hitpoints -= numero * 2
        print('Мой урон - ', self.hitpoints)

soldier = Sotilas(hitpoints=5)
man = Ihminen(hitpoints=5)
print(soldier)
soldier.loss(numero=1)
print(man)
man.loss(numero=1)

