# 1. Напишите функцию для транспонирования матрицы
# Пример:
# [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def matrix_transpose():
    rows_zip = zip(*matrix)
    transpose_matrix = [list(row) for row in rows_zip]
    return transpose_matrix


matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix_transpose())
