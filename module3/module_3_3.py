

def print_params(a = 1, b = 'Строка', c = True ):

    print(f"a = {a}, b = {b}, c = {c} ")



# ралзичные способы вызова функции
print_params(a = 2)
print_params(a = 2, b = 'Лист')
print_params(a = 2, b = 'Лист', c = False)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [15, "nope", [False, True, 2]]

values_dict = {'a': 100, 'b': 'fall', 'c': False}

# выписывание листа
print_params(*values_list)
# Выписывание словаря
print_params(**values_dict)

values_list2 = [99, "yes"]

print_params(*values_list2, 42)
