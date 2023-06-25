# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
# Пример:
# Ввод:
# 1/2
# 1/3
# Вывод:
# 5/6 1/6

import fractions

a = '1/2'
b = '1/3'

ZERO_NUM = 0
TWO_DUN = 2
MAX_LIMIT = 100
MIN_LIMIT = 1

dun_lst = []

numerator_first = int(a[ZERO_NUM])
dun_first = int(a[TWO_DUN])
numerator_second = int(b[ZERO_NUM])
dun_second = int(b[TWO_DUN])


def general_dun():
    if dun_first == dun_second:
        return dun_first
    else:
        for i in range(MIN_LIMIT, MAX_LIMIT):
            if i % dun_first == ZERO_NUM and i % dun_second == ZERO_NUM:
                dun_lst.append(i)
                res_sum_dun = min(dun_lst)
                return res_sum_dun


def sum_fraction():
    if dun_first == dun_second:
        if dun_first == numerator_first + numerator_second:
            return int((numerator_first + numerator_second) / general_dun())
        else:
            return numerator_first + numerator_second
    else:
        numerator_sum_first = numerator_first * int(general_dun() / dun_first)
        numerator_sum_second = numerator_second * int(general_dun() / dun_second)
        res_sum_numerator = numerator_sum_first + numerator_sum_second
        return res_sum_numerator


def prod_fraction_numerator():
    res_prod_numerator = numerator_first * numerator_second
    res_prod_dun = dun_first * dun_second
    if res_prod_dun % res_prod_numerator == 0:
        return int(res_prod_numerator/res_prod_numerator)
    else:
        return res_prod_numerator


def prod_fraction_dun():
    res_prod_numerator = numerator_first * numerator_second
    res_prod_dun = dun_first * dun_second
    if res_prod_dun % res_prod_numerator == 0:
        return int(res_prod_dun / res_prod_numerator)
    else:
        return res_prod_dun


if general_dun() == numerator_first + numerator_second:
    print(int(sum_fraction()), end=' ')
    print(f'{prod_fraction_numerator()}/{dun_first * dun_second}')
else:
    print(f'{sum_fraction()}/{general_dun()} {prod_fraction_numerator()}/{prod_fraction_dun()}')


d = fractions.Fraction(numerator_first, dun_first)
e = fractions.Fraction(numerator_second, dun_second)
print(d + e, d * e)