# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке

FIRST_VALUE = 2
SECOND_VALUE = 2

while SECOND_VALUE <= 10:
    print(f'{FIRST_VALUE} * {SECOND_VALUE} = {SECOND_VALUE * FIRST_VALUE}')
    SECOND_VALUE += 1
    if SECOND_VALUE == 11:
        if FIRST_VALUE < 9:
            FIRST_VALUE += 1
            SECOND_VALUE = 2
            print()
