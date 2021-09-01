def dimension_builder():
    dimensions_str = input().split()
    return [int(n) for n in dimensions_str]

def matrix_builder(dimensions):
    matrix = []
    for i in range(dimensions[0]):
        row_str = input().split()
        row = [int(n) for n in row_str]
        matrix.append(row)
    return matrix

def matrix_sum(matrix_1, matrix_2):
    answer = []
    for n in range(len(matrix_1)):
        row = [matrix_1[n][m] + matrix_2[n][m] for m in range(len(matrix_1[0]))]
        answer.append(row)
    return answer

def print_matrix(matrix):
    for n in range(len(matrix)):
        print(' '.join([str(m) for m in matrix[n]]))

dimensions_1 = dimension_builder()
matrix_1 = matrix_builder(dimensions_1)
dimensions_2 = dimension_builder()
matrix_2 = matrix_builder(dimensions_2)
if dimensions_1 == dimensions_2:
    matrix_sum = matrix_sum(matrix_1, matrix_2)
    print_matrix(matrix_sum)
else:
    print('ERROR')
