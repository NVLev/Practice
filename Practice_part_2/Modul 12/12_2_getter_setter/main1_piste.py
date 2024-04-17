# объект «Точка» на плоскости имеет координаты x и y; при создании новой точки могут передаваться
# пользовательские значения координат, по умолчанию x = 0, y = 0.
class Piste:
    count = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Piste.count += 1

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def check_value(self, value):
        if isinstance(value, str) and value.isdigit():
            value = float(value)
        if isinstance(value, (int, float)):
            return value
        return None

    def set_x(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__x = checker_value

    def set_y(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__y = checker_value


piste_1 = Piste()
piste_1.set_x('2')
piste_1.set_y('3')
print(piste_1)
