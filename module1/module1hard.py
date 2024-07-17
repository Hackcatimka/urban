#Вводные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#Делаем из множества в список для сортировки по алфавиту и создаем пустой словарь
students_list = [set(students)]
dict = {}

# Соортируем по алфавиту
students_list = sorted(students)

# Делаем цикл для работы с Массивами ставим условие по длине оценок, высчитываем среднюю оценку и добавляем в словарь ключ и его значение
for i in range(len(grades)):
    average = sum(grades[i]) / len(grades[i])
    dict.update({students_list[i]: average})

# Выводим результат
print("Словарь: ", dict)