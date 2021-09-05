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

    def matrix_builder(self, is_float=False):
        if self.which_matrix is None:
            print('Enter matrix:')
        else:
            print(f'Enter {self.which_matrix} matrix:')
        matrix = []
        for i in range(self.dimensions[0]):
            row_str = input().split()
            if is_float:
                row = [float(n) for n in row_str]
            else:
                row = [int(n) for n in row_str]
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
        constant = float(input('Enter constant: '))
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

class Menu:
    def __init__(self):
        self.choices = {
            "1": self.add_matrices,
            "2": self.multiply_by_constant,
            "3": self.multiply_matrices,
            "0": self.exit
        }

    def display_menu(self):
        print('1. Add matrices')
        print('2. Multiply matrix by a constant')
        print('3. Multiply matrices')
        print('0. Exit')

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
        matrix_1.matrix_builder(is_float=True)
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

    def exit(self):
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
# matrix_1 = Matrix(which_matrix='first')
# matrix_1.dimension_builder()
# matrix_1.matrix_builder()
# matrix_2 = Matrix(which_matrix='second')
# matrix_2.dimension_builder()
# matrix_2.matrix_builder()
# matrix_solution = MatrixAction()
# matrix_solution.matrix_multiplication(matrix_1, matrix_2)
# matrix_solution.print_matrix()

# matrix_1 = Matrix(which_matrix='first')
# matrix_1.dimension_builder()
# matrix_1.matrix_builder()
# matrix_solution = MatrixAction()
# matrix_solution.matrix_constant_multiplication(matrix_1)
# matrix_solution.print_matrix()

# matrix_1 = Matrix(which_matrix='first')
# matrix_1.dimension_builder()
# matrix_1.matrix_builder()
# matrix_2 = Matrix(which_matrix='second')
# matrix_2.dimension_builder()
# matrix_2.matrix_builder()
# matrix_solution = MatrixAction()
# matrix_solution.matrix_sum(matrix_1, matrix_2)
# matrix_solution.print_matrix()
