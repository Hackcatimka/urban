def personal_sum(numbers):
    """Подсчитывает сумму чисел в коллекции и количество некорректных данных."""
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item  # Пробуем сложить, предполагая, что item — число
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {item}")
            incorrect_data += 1  # Увеличиваем счетчик некорректных данных

    return result, incorrect_data


def calculate_average(numbers):
    """Вычисляет среднее арифметическое всех чисел в коллекции."""
    try:
        # Используем personal_sum для подсчёта суммы чисел
        total, incorrect_data = personal_sum(numbers)
        return total / len(numbers)  # Среднее значение
    except ZeroDivisionError:
        # Обрабатываем деление на 0 (пустая коллекция)
        return 0
    except TypeError:
        # Обрабатываем случай, когда передан не итератор
        print("В numbers записан некорректный тип данных")
        return None


# Примеры использования
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но символы не числа
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только числа
print(f'Результат 3: {calculate_average(567)}')  # Передан не итератор
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё корректно
