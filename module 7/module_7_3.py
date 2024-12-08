import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        """Возвращает словарь всех слов из файлов."""
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Считываем весь текст, переводим в нижний регистр и убираем пунктуацию
                    text = file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(punct, '')
                    # Разбиваем текст на слова
                    words = text.split()
                    # Добавляем в словарь
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []  # Если файл не найден, записываем пустой список

        return all_words

    def find(self, word):
        """Находит первое вхождение слова в каждом файле."""
        word = word.lower()  # Игнорируем регистр
        result = {}

        for name, words in self.get_all_words().items():
            try:
                position = words.index(word) + 1  # Индексация с 1
                result[name] = position
            except ValueError:
                result[name] = None  # Если слова нет, записываем None

        return result

    def count(self, word):
        """Подсчитывает количество вхождений слова в каждом файле."""
        word = word.lower()  # Игнорируем регистр
        result = {}

        for name, words in self.get_all_words().items():
            count = words.count(word)
            result[name] = count

        return result


# Пример использования
if __name__ == "__main__":
    # Создаем объект для анализа файлов
    finder = WordsFinder('test_file.txt')

    # Считываем все слова
    print(finder.get_all_words())

    # Ищем первое вхождение слова
    print(finder.find('TEXT'))

    # Подсчитываем количество слова
    print(finder.count('teXT'))
