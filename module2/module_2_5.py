# Создаем функцию с запросом значение
def get_matrix(n, m, value):
    matrix = []
    # Проверка на то что нету отрицательных чисел или нуля в запросе
    if value > 0 or n > 0 or m > 0:
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(value)
    else:
        print("Присутствует отрицательное значение: ", matrix)
    return matrix

# примеры запросов
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
