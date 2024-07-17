
my_dict = {2004:"Andrey",
           2006:"Mark",
           2001:"Tema"

}

print("Словарь: ", my_dict)

print("Вывод по существующему ключу: ", my_dict[2004])
print("Вывод без ошибки: ", my_dict.get(2002))

my_dict.update({2002:"Makentosh", 1999:"Horek"})
print("Обновленный словарь: ", my_dict)

del my_dict[2001]
print("Удаленный один элемент: ", my_dict)

my_set = {1, 2, 2.15, "Кот", 1, "Собака", "Кот", 5}
print("Множество: ", my_set)

my_set.add((1, 5, 6))
my_set.add("Уникальность")
print("Обновленное множество: ", my_set)

my_set.discard("Уникальность")
print("Обновленное множество удален один элемент (Уникальность): ", my_set)