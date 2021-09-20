import sys

class Matrix:
    def __init__(self, which_matrix=None):
        self.dimensions = None
        self.num_rows = None
        self.num_columns = None
        self.matrix = None
        self.which_matrix = which_matrix

    def dimension_builder(self):
        if self.which_matrix is None:
            dimensions_str = input(f'Enter size of matrix: ').split()
        else:
            dimensions_str = input(f'Enter size of {self.which_matrix} matrix: ').split()
        self.dimensions = [int(n) for n in dimensions_str]
        self.num_rows = self.dimensions[0]
        self.num_columns = self.dimensions[1]

    def matrix_builder(self):
        if self.which_matrix is None:
            print('Enter matrix:')
        else:
            print(f'Enter {self.which_matrix} matrix:')
        matrix = []
        for i in range(self.dimensions[0]):
            row_str = input().split()
            row = [float(n) if '.' in n else int(n) for n in row_str]
            matrix.append(row)
        self.matrix = matrix

    def print_matrix(self):
        print('The result is:')
        for n in range(len(self.matrix)):
            print(' '.join([str(m) for m in self.matrix[n]]))
        print()

class MatrixAction(Matrix):
    def matrix_sum(self, matrix_1, matrix_2):
        answer = []
        for n in range(len(matrix_1.matrix)):
            row = [matrix_1.matrix[n][m] + matrix_2.matrix[n][m] for m in range(len(matrix_1.matrix[0]))]
            answer.append(row)
        self.matrix = answer

    def matrix_constant_multiplication(self, matrix):
        constant_str = input('Enter constant: ')
        if '.' in constant_str:
            constant = float(constant_str)
        else:
            constant = int(constant_str)
        answer = []
        for n in range(len(matrix.matrix)):
            row = [constant * matrix.matrix[n][m] for m in range(len(matrix.matrix[0]))]
            answer.append(row)
        self.matrix = answer

    def matrix_multiplication(self, matrix_1, matrix_2):
        answer = []
        for n in range(matrix_1.num_rows):
            row = []
            for k in range(matrix_2.num_columns):
                element = 0
                for m in range(matrix_2.num_rows):
                    element += matrix_1.matrix[n][m] * matrix_2.matrix[m][k]
                row.append(element)
            answer.append(row)
        self.matrix = answer

    def transpose_main_diagonal(self):
        answer = [i[:] for i in self.matrix]
        for n in range(self.num_rows):
            for m in range(self.num_columns):
                answer[n][m] = self.matrix[m][n]
        self.matrix = answer

    def transpose_side_diagonal(self):
        answer = [i[:] for i in self.matrix]
        for n in range(self.num_rows):
            for m in range(self.num_columns):
                answer[n][m] = self.matrix[-m - 1][-n - 1]
        self.matrix = answer

    def transpose_vertical_line(self):
        self.matrix = [i[::-1] for i in self.matrix]

    def transpose_horizontal_line(self):
        self.matrix = self.matrix[::-1]

    def get_determinant(self, matrix_1):
        if matrix_1.num_rows == 1:
            return matrix_1.matrix[0][0]
        elif matrix_1.num_rows == 2:
            return matrix_1.matrix[0][0] * matrix_1.matrix[1][1] - matrix_1.matrix[1][0] * matrix_1.matrix[0][1]
        else:
            determinant = 0
            for j in range(matrix_1.num_columns):
                cofactor = (-1) ** (j) * matrix_1.matrix[0][j]
                minor = Matrix()
                minor.matrix = [matrix_1.matrix[i][:j] + matrix_1.matrix[i][j + 1:] for i in range(matrix_1.num_rows) if i != 0]
                minor.num_rows = len(minor.matrix)
                minor.num_columns = len(minor.matrix[0])
                minor.dimensions = [minor.num_rows, minor.num_columns]
                determinant += cofactor * self.get_determinant(minor)
            return determinant



class Menu:
    def __init__(self):
        self.choices = {
            "1": self.add_matrices,
            "2": self.multiply_by_constant,
            "3": self.multiply_matrices,
            "4": self.transpose_matrix,
            "5": self.calculate_determinant,
            "0": self.exit
        }

    def display_menu(self):
        print('1. Add matrices')
        print('2. Multiply matrix by a constant')
        print('3. Multiply matrices')
        print('4. Transpose matrix')
        print('5. Calculate a determinant')
        print('0. Exit')

    def transpose_display_menu(self):
        print()
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')

    def run(self):
        while True:
            self.display_menu()
            user_input = input('Your choice: ').strip()
            action = self.choices.get(user_input)
            if action:
                action()
            else:
                print('Not a valid choice\n')

    def add_matrices(self):
        matrix_1 = Matrix(which_matrix='first')
        matrix_1.dimension_builder()
        matrix_1.matrix_builder()
        matrix_2 = Matrix(which_matrix='second')
        matrix_2.dimension_builder()
        matrix_2.matrix_builder()
        if matrix_1.dimensions == matrix_2.dimensions:
            matrix_solution = MatrixAction()
            matrix_solution.matrix_sum(matrix_1, matrix_2)
            matrix_solution.print_matrix()
        else:
            print('The operation cannot be performed.\n')

    def multiply_by_constant(self):
        matrix_1 = Matrix()
        matrix_1.dimension_builder()
        matrix_1.matrix_builder()
        matrix_solution = MatrixAction()
        matrix_solution.matrix_constant_multiplication(matrix_1)
        matrix_solution.print_matrix()

    def multiply_matrices(self):
        matrix_1 = Matrix(which_matrix='first')
        matrix_1.dimension_builder()
        matrix_1.matrix_builder()
        matrix_2 = Matrix(which_matrix='second')
        matrix_2.dimension_builder()
        matrix_2.matrix_builder()
        if matrix_1.num_columns == matrix_2.num_rows:
            matrix_solution = MatrixAction()
            matrix_solution.matrix_multiplication(matrix_1, matrix_2)
            matrix_solution.print_matrix()
        else:
            print('The operation cannot be performed.\n')

    def transpose_matrix(self):
        self.transpose_display_menu()
        user_input = input('Your choice: ').strip()
        if user_input not in '1234':
            print('Not a valid choice\n')
        else:
            matrix = MatrixAction()
            matrix.dimension_builder()
            matrix.matrix_builder()
            if user_input == '1':
               matrix.transpose_main_diagonal()
            elif user_input == '2':
                matrix.transpose_side_diagonal()
            elif user_input == '3':
                matrix.transpose_vertical_line()
            else:
                matrix.transpose_horizontal_line()
            matrix.print_matrix()

    def calculate_determinant(self):
        matrix = Matrix()
        matrix.dimension_builder()
        matrix.matrix_builder()
        print('The result is:')
        print(MatrixAction().get_determinant(matrix))
        print()

    def exit(self):
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
