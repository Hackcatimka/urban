# Base class Vehicle
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in map(str.lower, self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


# Subclass Sedan inheriting from Vehicle
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


# Testing the classes
if __name__ == "__main__":
    # Initial vehicle
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Initial properties
    vehicle1.print_info()

    # Changing properties
    vehicle1.set_color('Pink')  # Invalid color
    vehicle1.set_color('BLACK')  # Valid color
    vehicle1.owner = 'Vasyok'

    # Final properties
    vehicle1.print_info()
