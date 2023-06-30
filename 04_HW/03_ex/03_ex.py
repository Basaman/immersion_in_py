from utils import *

MODES = """Действия:
пополнение - i
снятие - g
выйти - q
Выберите действие: """


def main():
    while True:
        choose = input(f"{MODES}")
        if balance >= LUXURY_LIMIT:
            luxury()
        if operations_count % OPERATIONS_FOR_BONUS == 0:
            bonus()
        if choose == 'i':
            money_input()
        elif choose == 'g':
            money_get()
        elif choose == 'q':
            break
        else:
            print(f'Incorrect')


main()
