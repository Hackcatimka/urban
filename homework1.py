example = "Круто"

print("Слово Примернный \nПервый символ: ", example[0])
print("Последний символ: ", example[-1])
mid = int(len(example)/2)
print("Вторая половина строки: ", example[mid::])
print("Слово наоборот: ", example[::-1])
print("Каждый второй символ: ", example[::2])