# Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
#Добавьте методы для сложения, вычитания и умножения матриц.

class Matrix:
    def __init__(self, data):

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны совпадать для сложения")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны совпадать для вычитания")
        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "Число столбцов первой матрицы должно быть равно числу строк второй"
            )
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __repr__(self):

        return "\n".join(["\t".join(map(str, row)) for row in self.data])


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
print("Сложение:\n", m1.add(m2))
print("Вычитание:\n", m1.subtract(m2))
m3 = Matrix([[1, 0, 2], [-1, 3, 1]])
m4 = Matrix([[3, 1], [2, 1], [1, 0]])
print("Умножение:\n", m3.multiply(m4))