import pandas as pd

# Загрузка данных из CSV файлов с обработкой ошибок
try:
    # Попробуем определить правильный разделитель, предположительно ','
    rister = pd.read_csv('rister.csv', sep=',', on_bad_lines='skip')
    dvs = pd.read_csv('dvs.csv', sep=',', on_bad_lines='skip')
except pd.errors.ParserError as e:
    print("Ошибка при чтении CSV файлов:", e)
    exit()

# Предполагаем, что столбцы называются 'Название сделки' и 'Контакт: Мобильный телефон'
rister_columns = ['Название сделки', 'Контакт: Мобильный телефон']
dvs_columns = ['Название сделки', 'Контакт: Мобильный телефон']

# Проверяем, что нужные столбцы есть в обоих таблицах
if all(col in rister.columns for col in rister_columns) and all(col in dvs.columns for col in dvs_columns):
    # Обновляем телефоны в таблице dvs
    for index, row in rister.iterrows():
        matching_rows = dvs[dvs['Название сделки'] == row['Название сделки']]

        if not matching_rows.empty:
            if matching_rows.iloc[0]['Контакт: Мобильный телефон'] != row['Контакт: Мобильный телефон']:
                dvs.loc[dvs['Название сделки'] == row['Название сделки'], 'Контакт: Мобильный телефон'] = row[
                    'Контакт: Мобильный телефон']
        else:
            dvs = dvs.append(row, ignore_index=True)

    # Сохраняем обновленную таблицу
    dvs.to_csv('/mnt/data/updated_dvs.csv', index=False)
    "Телефоны успешно обновлены и сохранены в 'updated_dvs.csv'!"
else:
    "Ошибка: Входные файлы не содержат ожидаемых столбцов."
