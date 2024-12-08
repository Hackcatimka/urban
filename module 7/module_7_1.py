class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        """Читает все товары из файла и возвращает их в виде строки"""
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()  # Убираем лишние символы
        except FileNotFoundError:
            return ""  # Если файла нет, возвращаем пустую строку

    def add(self, *products):
        """Добавляет товары в файл, если их там еще нет"""
        # Получаем список текущих товаров в магазине
        current_products = self.get_products().split('\n')
        current_names = [line.split(', ')[0] for line in current_products if line]

        # Открываем файл для добавления
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in current_names:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(str(product) + '\n')


# Пример использования
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    # Вывод информации о продукте
    print(p2)  # Spaghetti, 3.4, Groceries

    # Добавление продуктов в магазин
    s1.add(p1, p2, p3)

    # Чтение текущих продуктов из магазина
    print(s1.get_products())
