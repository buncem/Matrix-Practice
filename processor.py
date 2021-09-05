class Matrix:
    def __init__(self, which_matrix=None):
        self.dimensions = None
        self.matrix = None
        self.which_matrix = which_matrix

    def dimension_builder(self):
        if self.which_matrix is None:
            dimensions_str = input(f'Enter size of matrix: ').split()
        else:
            dimensions_str = input(f'Enter size of {self.which_matrix} matrix: ').split()
        self.dimensions = [int(n) for n in dimensions_str]

    def matrix_builder(self):
        if self.which_matrix is None:
            print('Enter matrix:')
        else:
            print(f'Enter {self.which_matrix} matrix:')
        matrix = []
        for i in range(self.dimensions[0]):
            row_str = input().split()
            row = [int(n) for n in row_str]
            matrix.append(row)
        self.matrix = matrix

    def print_matrix(self):
        for n in range(len(self.matrix)):
            print(' '.join([str(m) for m in self.matrix[n]]))

class MatrixAction(Matrix):
    def matrix_sum(self, matrix_1, matrix_2):
        answer = []
        for n in range(len(matrix_1.matrix)):
            row = [matrix_1.matrix[n][m] + matrix_2.matrix[n][m] for m in range(len(matrix_1.matrix[0]))]
            answer.append(row)
        self.matrix = answer

    def matrix_constant_multiplication(self, matrix):
        constant = int(input('Enter constant: '))
        answer = []
        for n in range(len(matrix.matrix)):
            row = [constant * matrix.matrix[n][m] for m in range(len(matrix.matrix[0]))]
            answer.append(row)
        self.matrix = answer

#class Menu:

matrix_1 = Matrix(which_matrix='first')
matrix_1.dimension_builder()
matrix_1.matrix_builder()
matrix_solution = MatrixAction()
matrix_solution.matrix_constant_multiplication(matrix_1)
matrix_solution.print_matrix()

# matrix_1 = Matrix(which_matrix='first')
# matrix_1.dimension_builder()
# matrix_1.matrix_builder()
# matrix_2 = Matrix(which_matrix='second')
# matrix_2.dimension_builder()
# matrix_2.matrix_builder()
# matrix_solution = MatrixAction()
# matrix_solution.matrix_sum(matrix_1, matrix_2)
# matrix_solution.print_matrix()
