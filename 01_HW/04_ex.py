#  Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
random_number = randint(0, 1000)
user_ges_number = int(input('Отгадайте число: '))
count = 0
ATTEMPT = 10

while count < ATTEMPT -1:
    if random_number == user_ges_number:
        print('Ура!!!')
        break
    if random_number > user_ges_number:
        count += 1
        print(f'больше, осталось {ATTEMPT - count} попыток')
        print()
        user_ges_number = int(input('Отгадайте число: '))
    else:
        count += 1
        print(f'меньше, осталось {ATTEMPT - count} попыток')
        print()
        user_ges_number = int(input('Отгадайте число: '))

if count == ATTEMPT - 1:
    print('Увы, вы продули :((( ')


