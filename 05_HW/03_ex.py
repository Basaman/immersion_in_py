# Создайте функцию генератор чисел Фибоначчи


def fibo(limit: int) -> list:
    a, b = 0, 1
    for i in range(limit):
        yield a
        a, b = b, a + b


elements = 11
print(list(fibo(elements)))



