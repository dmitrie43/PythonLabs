"""
Выполнить обработку элементов прямоугольной матрицы A, имеющей N строк и M столбцов.
Найти сумму элементов всей матрицы.
Определить, какую долю в этой сумме составляет сумма элементов каждого столбца.
Результат оформить в виде матрицы из N + 1 строк и M столбцов.
"""

import numpy as np


def get_matrix(size, length_columns, length_rows):
    """
    get size matrix
    :param size:
    :param length_columns:
    :param length_rows:
    :return:
    """
    # matrix = np.array([
    #     [random.randrange(0, 10) for i in range(lengthColumns)] for j in range(lengthRows)
    # ], int)
    matrix = np.arange(size)
    matrix = matrix.reshape(length_columns, length_rows)
    return matrix


print('Введите размерность матрицы:')
matrixSize = int(input())
print('Введите кол-во строк:')
lengthRows = int(input())
print('Введите кол-во столбцов:')
lengthColumns = int(input())

matrix = get_matrix(matrixSize, lengthColumns, lengthRows)
print('Матрица:')
print(matrix)

amount = matrix.sum()
print("Сумма: " + str(amount))

amounts = sum(matrix)
print('Суммы каждого столбца:')
print(amounts)

percents = []
for number in amounts:
    percents.append(str(round(number / amount * 100, 2)) + '%')
print('Доли в процентах:')
print(percents)
