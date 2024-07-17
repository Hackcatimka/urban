

immutable_var = (10, 5.12, "Кортеж")

print("Кортеж: ", immutable_var, type(immutable_var))
try:
    immutable_var[0] = "10"
except TypeError as e:
    print(f"Ошибка: {e}. \nНельзя поменять значения потому что кортеж, является неизменяемой структорой данных, в основном предназначен для констант")



mutable_list = [2, 10.4, "Список"]
print("\nСписок до модификации: ",mutable_list)
mutable_list[1] = 15
mutable_list.append("Модифицирован")
print("Список после модификации: ", mutable_list)