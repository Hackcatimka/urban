def custom_write(file_name, strings):

    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_num, string in enumerate(strings, start=1):
            # Получаем текущую позицию указателя
            start_byte = file.tell()
            # Записываем строку с символом перехода на новую строку
            file.write(string + '\n')
            # Сохраняем информацию в словарь
            strings_positions[(line_num, start_byte)] = string

    return strings_positions


# Пример использования функции
if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
