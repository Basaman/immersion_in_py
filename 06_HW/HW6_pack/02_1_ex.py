# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях. Известно,
# что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from random import randint

N = 8
queens_coord_x = [randint(0, N-1) for i in range(N)]
queens_coord_y = [randint(0, N-1) for j in range(N)]

horizontal_repeat_lst = []
vertical_repeat_lst = []


def queens_attack():
    for i in range(N):
        qty = queens_coord_x.count(i)
        horizontal_repeat_lst.append(qty)
        for j in horizontal_repeat_lst:
            if j > 1:
                return False

    for i in range(N):
        qty = queens_coord_y.count(i)
        vertical_repeat_lst.append(qty)
        for j in vertical_repeat_lst:
            if j > 1:
                return False

    for i in range(N):
        for j in range(i + 1, N):
            if abs(queens_coord_x[i] - queens_coord_x[j]) == \
                    abs(queens_coord_y[i] - queens_coord_y[j]):
                return False
            else:
                return True


if __name__ == '__main__':
    print(queens_coord_x)
    print(queens_coord_y)
    print(queens_attack())
