# Задача 2:
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей.
# Ответьте на вопросы:
# ** какие вещи взяли все три друга
# ** какие вещи уникальны, есть только у одного друга
# ** какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

baggage = {
    'Denis': ('fishing rod', 'lighter', 'tent'),
    'Alex': ('tent', 'brazier', 'gun'),
    'Vlad': ('tent', 'gun', 'sun cream')
}

FR_1 = 0
FR_2 = 1
FR_3 = 2

all_items = list(baggage.values())
must_have_item = set.intersection(set(all_items[FR_1]), set(all_items[FR_2]), set(all_items[2]))
print(f'Все три друга взяли: {must_have_item}')
print()


first_friend_uniq_items = set(all_items[FR_1]) - set.union(set(all_items[FR_2]), set(all_items[FR_3]))
second_friend_uniq_items = set(all_items[FR_2]) - set.union(set(all_items[FR_1]), set(all_items[FR_3]))
third_friend_uniq_items = set(all_items[FR_3]) - set.union(set(all_items[FR_1]), set(all_items[FR_2]))
print(f'Уникальные вещи у Denis :\t{first_friend_uniq_items}')
print(f'Уникальные вещи у Alex :\t{second_friend_uniq_items}')
print(f'Уникальные вещи у Vlad :\t{third_friend_uniq_items}')
print()


except_one_friend_1 = set(all_items[FR_1]) - first_friend_uniq_items
except_one_friend_2 = set(all_items[FR_2]) - second_friend_uniq_items
except_one_friend_3 = set(all_items[FR_3]) - third_friend_uniq_items

if except_one_friend_1 == except_one_friend_2:
    print(f'у всех друзей есть {except_one_friend_1 - except_one_friend_3}, а у Vlad отсутсвует')
if except_one_friend_1 == except_one_friend_3:
    print(f'у всех друзей есть {except_one_friend_1 - except_one_friend_2} а у Alex отсутсвует')
if except_one_friend_3 == except_one_friend_2:
    print(f'у всех друзей есть {except_one_friend_3 - except_one_friend_1} а у Denis отсутсвует')
