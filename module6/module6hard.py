import math


# Базовый класс Figure
class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = False
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Некорректный цвет")

    def __is_valid_sides(self, *new_sides):
        return (
            len(new_sides) == self.sides_count
            and all(isinstance(side, (int, float)) and side > 0 for side in new_sides)
        )

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Стороны не изменены")


# Класс Circle, наследуется от Figure
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


# Класс Triangle, наследуется от Figure
class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2  # Полупериметр
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


# Класс Cube, наследуется от Figure
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            super().__init__(color, *(sides * self.sides_count))
        else:
            super().__init__(color, *([1] * self.sides_count))

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


# Проверка работы классов
if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # Цвет и стороны
    cube1 = Cube((222, 35, 130), 6)

    # Проверка изменения цветов
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())  # [55, 66, 77]
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())  # [222, 35, 130]

    # Проверка изменения сторон
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())  # [15]

    # Проверка периметра круга (длины окружности)
    print(len(circle1))  # 15

    # Проверка объёма куба
    print(cube1.get_volume())  # 216
