# Base class Animal
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

# Base class Plant
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

# Subclass Mammal inheriting from Animal
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Subclass Predator inheriting from Animal
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Subclass Flower inheriting from Plant
class Flower(Plant):
    pass

# Subclass Fruit inheriting from Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Override edible attribute

# Testing the classes and their interactions
if __name__ == "__main__":
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)  # Волк с Уолл-Стрит
    print(p1.name)  # Цветик семицветик

    print(a1.alive)  # True
    print(a2.fed)    # False

    a1.eat(p1)       # Волк с Уолл-Стрит не стал есть Цветик семицветик
    a2.eat(p2)       # Хатико съел Заводной апельсин

    print(a1.alive)  # False
    print(a2.fed)    # True
