
first = input("Введите первое число - ")
second = input("Введите второе число - ")
third = input("Введите треть число - ")

if first == second == third:
    print("Три одинаковых числа")
elif first == second or first == third or second == third:
    print("Два числа одинаковых")
else:
    print("Нету одинаковых чисел")

