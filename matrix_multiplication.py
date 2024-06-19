A = [
    [14, 8, 9],
    [1, 78, 9],
    [7, 8, 9]
]

B = [
    [1],
    [2],
    [2]
]

a = [1, 8, 9]

b = [1, 4, 7]


def matrix_size(A):
    n, m = len(A), len(A[0])
    return n, m


def new_matrix_size(A, B):
    """
        Considers what size the A*B matrix should be, if product is legal
    """
    size_A = matrix_size(A)
    size_B = matrix_size(B)
    if size_A[1] != size_B[0]:
        print('This Matrices Cant be Multiplied')
        return None
    return (size_A[0], size_B[1])


def generate_new_matrixs_form(A, B):
    """
        Generating matrix of zeros with size of A*B
    """
    M = []
    size = new_matrix_size(A, B)
    if size is None:
        return
    for _ in range(size[0]):
        M.append([0] * size[1])
    return M


def transposed_matrix_form(A):
    n, m = matrix_size(A)
    return m, n


def generate_transposed_matrixs_form(A):
    """
        Generating matrix of zeros with size of A transposed
    """
    T = []
    n, m = transposed_matrix_form(A)
    for _ in range(n):
        T.append(m * [0])
    return T


def my_matrix_transpose(A):
    """
    Calculating the transpose of matrix A
    """
    i = 0
    T = generate_transposed_matrixs_form(A)
    for row in T:
        for j in range(len(row)):
            row[j] = A[j][i]
        i += 1
    return T


def my_dot_product(a, b):
    """
    Calculating dot product of a and b, if its legal
    """
    dot_product = 0
    if len(a) != len(b):
        print('This vectors cant have dot product')
        return
    for i in range(len(a)):
        dot_product += a[i] * b[i]
    return dot_product


def my_matrix_mult(A, B):
    """
    Calculating product of matrices A and B
    """
    M = generate_new_matrixs_form(A, B)

    if M is None:
        return

    B_T = my_matrix_transpose(B)

    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = my_dot_product(A[i], B_T[j])
    return M


print(my_matrix_mult(A, B))
