class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Добавляем название здания в список истории
        if args:
            cls.houses_history.append(args[0])
        # Создаем новый объект
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        # Вывод сообщения при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")


# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # Ожидается: ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # Ожидается: ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # Ожидается: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаляем объекты
del h2
del h3

# Проверяем историю зданий
print(House.houses_history)  # Ожидается: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
