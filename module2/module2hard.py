# Вводим значение от 3 до 20
n = int(input ("Введите число от 3 до 20: "))
# Переменная для хранения результата
res = ""

for i in range(1,n):
    for j in range(i+1, n+1):
        # складываем значение, чтобы потом проверить их кратность выбраному числу
        x = i+j
        if n/x == 1: # проверка кратности числу
            res += str(i) + str(j)

print(res)