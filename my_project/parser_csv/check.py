import pandas as pd

# Загрузка данных из CSV файла
rister = pd.read_csv('rister2.csv', sep=',', on_bad_lines='skip')

# Выводим список столбцов
print(rister.columns.tolist())
