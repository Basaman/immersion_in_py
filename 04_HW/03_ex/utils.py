balance = 0
operations_count = 0
MONEY_DIV = 50
TAX_OUTCOME = 0.015
MAX_TAX_OUT = 600
MIN_TAX_OUT = 30
LUXURY_LIMIT = 5_000_000
TAX_LUXURY = 0.9
BONUS_FOR_OPERATION = 1.03
OPERATIONS_FOR_BONUS = 3


def money_input():
    global balance, operations_count
    income = int(input('Введите сумму внесения: '))
    if income % MONEY_DIV == 0:
        balance += income
        print(f'Ваш баланс равен: {balance}')
        return balance
    else:
        print(f'Нееверная сумма внесения, ваш баланс равен {balance}')
    operations_count += 1
    return balance


def money_get():
    global balance, operations_count
    outcome = int(input('Введите сумму снятия: '))
    if outcome % MONEY_DIV == 0:
        comission = balance * TAX_OUTCOME
        if comission >= MAX_TAX_OUT:
            comission = MAX_TAX_OUT
        elif comission <= MIN_TAX_OUT:
            comission = MIN_TAX_OUT
        balance -= comission
        balance -= outcome
        print(f'Ваш баланс равен: {balance}')
        return balance
    else:
        print(f'Нееверная сумма снятия, ваш баланс равен {balance}')
    operations_count += 1
    return balance


def luxury():
    global balance
    balance *= TAX_LUXURY
    print('Раскулачивание')
    return balance


def bonus():
    global balance
    balance *= BONUS_FOR_OPERATION
    print('Бонус за 3 операции')
    return balance
