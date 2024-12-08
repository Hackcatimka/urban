import random

# Базовый класс Animal
class Animal:
    # Атрибуты класса
    live = True  # Живой организм
    sound = None  # Звук, который издает животное
    _DEGREE_OF_DANGER = 0  # Степень опасности (по умолчанию 0)

    def __init__(self, speed):
        # Координаты в пространстве
        self._cords = [0, 0, 0]
        # Скорость движения
        self.speed = speed

    # Метод для движения животного
    def move(self, dx, dy, dz):
        # Рассчитываем новое значение по оси Z
        new_z = self._cords[2] + dz * self.speed
        # Проверяем, если координата Z уходит в отрицательное значение
        if new_z < 0:
            print("Слишком глубоко :(")  # Слишком глубоко
        else:
            # Изменяем координаты X, Y, Z
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    # Метод для вывода текущих координат
    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    # Метод атаки
    def attack(self):
        # Если степень опасности меньше 5, животное мирное
        if self._DEGREE_OF_DANGER < 5:
            print("Безопасно :)")
        else:
            # Если степень опасности >= 5, животное атакует
            print("Осторожно, могут атаковать")


# Класс Bird (птица), наследуется от Animal
class Bird(Animal):
    # Атрибут наличия клюва
    beak = True

    # Метод откладывания яиц
    def lay_eggs(self):
        # Случайное количество яиц от 1 до 4
        eggs = random.randint(1, 4)
        print(f"Здесь  {eggs} яица для тебя")


# Класс AquaticAnimal (водное животное), наследуется от Animal
class AquaticAnimal(Animal):
    # Степень опасности для водных животных
    _DEGREE_OF_DANGER = 3

    # Метод для ныряния
    def dive_in(self, dz):
        # Всегда берем модуль dz, чтобы сделать его положительным
        dz = abs(dz)
        # Рассчитываем новое значение по оси Z с учетом уменьшенной скорости (speed / 2)
        new_z = self._cords[2] - dz * (self.speed / 2)
        # Проверяем, если координата Z уходит в отрицательное значение
        if new_z < 0:
            print("Слишком глубоко")  # Слишком глубоко
        else:
            # Изменяем координату Z
            self._cords[2] = new_z


# Класс PoisonousAnimal (ядовитое животное), наследуется от Animal
class PoisonousAnimal(Animal):
    # Степень опасности для ядовитых животных
    _DEGREE_OF_DANGER = 8


# Класс Duckbill (утконос), наследуется от Bird, AquaticAnimal, PoisonousAnimal
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        # Инициализируем родительские классы
        super().__init__(speed)
        # Атрибут звука, издаваемого утконосом
        self.sound = "*звук утконоса*"

    # Метод для издания звука
    def speak(self):
        print(self.sound)


# Тестирование классов
if __name__ == "__main__":
    # Создаем объект утконоса с заданной скоростью
    db = Duckbill(10)

    # Проверяем базовые свойства
    print(db.live)  # True (живой)
    print(db.beak)  # True (наличие клюва)

    # Утконос издает звук
    db.speak()  # Click-click-click
    # Проверяем атаку
    db.attack()  # Be careful, I'm attacking you 0_0

    # Перемещение утконоса
    db.move(1, 2, 3)
    db.get_cords()  # X: 10 Y: 20 Z: 30

    # Утконос ныряет
    db.dive_in(6)
    db.get_cords()  # X: 10 Y: 20 Z: 0

    # Утконос откладывает яйца
    db.lay_eggs()  # Случайное количество яиц от 1 до 4
