#Создание базового класса "Фигура" и его наследование для создания классов "Квадрат", "Прямоугольник" и "Круг".
#Класс "Фигура" будет иметь общие методы, такие как вычисление площади и периметра, а классы-наследники будут иметь специфичные методы и свойства.

class Figura:
    """Базовый класс для всех фигур"""

    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def perimeter(self):
        return 0

    def info(self):
        print(f"Фигура: {self.name}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")


class Kvadrat(Figura):
    """Класс для квадрата"""

    def __init__(self, side):
        super().__init__("Квадрат")
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Pryamougolnik(Figura):
    """Класс для прямоугольника"""

    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Krug(Figura):
    """Класс для круга"""

    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


kv = Kvadrat(5)
print("Площадь квадрата:", kv.area())
print("Периметр квадрата:", kv.perimeter())

kv = Pryamougolnik(4, 6)
print("Площадь прямоугольника:", kv.area())
print("Периметр прямоугольника:", kv.perimeter())

kv = Krug(3)
print("Площадь круга:", kv.area())
print("Периметр круга:", kv.perimeter())
