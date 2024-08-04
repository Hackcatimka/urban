
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total = 0

def calculate_structure_sum(data_structure):


    def recursive(item):
        global total

        if isinstance(item, str):
            total += len(item)
        elif isinstance(item, int):
            total += item
        elif isinstance(item, (list, tuple, set)):
            for elem in item:
                recursive(elem)
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive(key)
                recursive(value)

    recursive(data_structure)
    return total


result = calculate_structure_sum(data_structure)
print(result)  
