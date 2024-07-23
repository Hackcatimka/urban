# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создание пустых списков для простых и непростых чисел
primes = []
not_primes = []

# Перебираем числа из исходного списка
for num in numbers:
    if num == 1:
        continue

    is_prime = True

    # Проверяем делители от 2 до num - 1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Записываем число в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки простых и непростых чисел
print("Primes:", primes)
print("Not Primes:", not_primes)
