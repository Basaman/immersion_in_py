# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))

ZERO = 0
SIXTEEN = 16
CONST_HEX_VAL = {10: 'a', 11: "b", 12: "c", 13: 'd', 14: 'e', 15: 'f'}

num_hex_dict = {}

print(hex(num))

while num > ZERO:
    num_hex_val = num % SIXTEEN
    num = num // SIXTEEN
    num_hex_dict[num] = num_hex_val

num_hex_dict = dict(reversed(num_hex_dict.items()))
num_hex_dict = dict.values(num_hex_dict)

print('0x', end='')

for i in num_hex_dict:
    for j in dict.keys(CONST_HEX_VAL):
        if i == j:
            i = CONST_HEX_VAL[j]
    print(i, end='')
