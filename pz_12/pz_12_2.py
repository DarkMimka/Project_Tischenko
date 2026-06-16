#В матрице найти сумму элементов первых двух строк.

def sum_first_two_rows(matrix):
    if not matrix:
        return 0

    first_two_rows = matrix[:2]

    return sum(map(sum, first_two_rows))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Сумма первых двух строк:", sum_first_two_rows(matrix))