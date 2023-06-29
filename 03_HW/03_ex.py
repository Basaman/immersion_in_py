# Дополнительно:
# Задача 1:
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# Верните все возможные варианты комплектации рюкзака.

import random

trip_things_dict = {'палатка': 5, 'спальник': 1, 'кастрюля': 2, 'нож': 1, 'консервы': 2, 'греча': 1,
                    'картофель': 1, 'морковь': 1, 'лук': 1, 'специи': 0.4}

MAX_LOAD_CAPACITY = 10
bag_weight = 0

trip_things_list = list(trip_things_dict.items())
random.shuffle(trip_things_list)


for k, v in trip_things_list:
    if v <= MAX_LOAD_CAPACITY:
        print(f'вещь: {k}; вес: {v} кг')
        MAX_LOAD_CAPACITY -= v
        bag_weight += v

print(f'итого: {bag_weight} кг')






