def add_everything_up(a, b):
    try:
        # Пытаемся сложить значения стандартным образом
        return a + b
    except TypeError:
        # Обрабатываем случай, когда типы данных разные (например, число и строка)
        return f"{a}{b}"

# Пример использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))    # Вывод: яблоко4215
print(add_everything_up(123.456, 7))        # Вывод: 130.456
