# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии (решение задачи "не в одну строку"
# есть на 4 семинаре(5 задача))

names = ['Ivan', 'Vlad', 'Semen', 'Roman', 'Bob']
rates = [1000, 500, 200, 900, 400]
bonuses = ['10.25%', '7.14%', '8.9%', '2.3%', '5.5%']

new_dict_2 = {name: round((rate * bonus), 2) for name, rate, bonus in zip
              (names, rates, (float(i.replace('%', '')) / 100 for i in bonuses))}
print(new_dict_2)


# bonus_fl = []
# for i in bonuses:
#     bonus_fl.append(float(i.replace('%', '')) / 100)
#
#
# new_dict = dict()
# for name, rate, bonus in zip(names, rates, bonus_fl):
#     new_dict[name] = round((rate * bonus), 2)
#
# print(new_dict)



