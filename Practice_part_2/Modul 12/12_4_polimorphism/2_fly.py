# Реализуйте класс «Может летать».
#
# Лететь (в теле прописать pass).
# Приземлиться (установить высоту и скорость в значение 0). Вывести высоту и скорость на экран.
#
# Затем реализуйте два дочерних класса:
#
# «Бабочка», который может:
#
# Взлететь (высота = 1). Лететь (скорость = 0.5). «Ракета», которая может:
#
# Взлететь (высота = 500, скорость = 1000). Приземлиться (высота = 0, взрыв).
# Взорваться (тут уже что угодно).
class Voilenne:
    Title = 'Voilenne'
    def __init__(self, korkeus=0, nopeus=0 ):
        self.korkeus = korkeus
        self.nopeus = nopeus

    def nousta(self):
        pass

    def lenne(self):
        pass

    def laskeutua(self):
        print('Laskeutun')
        self.korkeus = 0
        self.nopeus = 0

    def __str__(self):
        return 'Olen {}. Minun korkeus on {}, minun nopeus on {}'.format(self.Title, self.korkeus, self.nopeus)

class Perhonen(Voilenne):
    Title = 'Perhonen'
    def __init__(self):
        super().__init__()

    def nousta(self):
        print('Nouseen')
        self.korkeus = 1

    def lenne(self):
        print('Lennän')
        self.nopeus = 0.5

class Raketti(Voilenne):
    Title = 'Raketti'
    def nousta(self):
        print('Nouseen')
        self.korkeus = 500

    def lenne(self):
        print('Lennän')
        self.nopeus = 1000

    def laskeutua(self):
        print('Laskeutun')
        self.korkeus = 0
        print('Purkaus')

    def purkaus(self):
        print('Ba-ba-bam!')

butterfly = Perhonen()
butterfly.nousta()
print(butterfly)
butterfly.lenne()
print(butterfly)
butterfly.laskeutua()
print(butterfly)
rocket = Raketti()
rocket.nousta()
print(rocket)
rocket.lenne()
print(rocket)
rocket.laskeutua()
print(rocket)
rocket.purkaus()


