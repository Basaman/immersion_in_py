# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
# Пример:
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

my_list = [1, 2, 3, 1, 2, 4, 5]
my_dict = {}
new_list = []
MIN_REPEAT = 1

for i in my_list:
    my_dict[i] = my_list.count(i)


for i in my_dict:
    if my_dict[i] > MIN_REPEAT:
        new_list.append(i)

print(f'{my_list} -> {new_list}')




