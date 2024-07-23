
calls = 0

# функция для подсчета вызовов других функций
def count_calls():
    global calls

    calls += 1
# Функция которая из строки делает кортеж с таким значения: длина строки, Верхний регистр, Нижний регистр
def string_info(string):
    count_calls()
    list = [len(string), string.upper(), string.lower()]
    my_tuple = tuple(list)



    return my_tuple

# Функция для проверки, есть ли в списке выбранное слово
def is_contains(string, list_to_search):
    count_calls()
    for element in list_to_search:
        element = element.lower()
        string = string.lower()
        if element == string:
            return True
    return False

# Примеры
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)