# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')


def file_way(text: str) -> tuple:
    *address, suffix = text.split('/')
    file, file_extension = suffix.split('.')
    address = str(address).replace(', ', '/')\
                          .replace("'", '')\
                          .replace('[', '')\
                          .replace(']', '') + '/'
    text_tuple = tuple([address, file, file_extension])
    return text_tuple


file_address = 'c:/Users/Vladislav/Desktop/deep_to_python/test.txt'
print(file_way(file_address))
