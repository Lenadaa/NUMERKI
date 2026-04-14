def gaussian_elimination(A, b):
    n = len(A)
    matrix = append_matrix(A, b)
    eps = 1e-10

    for k in range(n):

        max_id = find_max(matrix, k)
        swap_rows(matrix, max_id, k)

        if abs(matrix[k][k]) < eps:
            continue

        eliminate_row(matrix, k)

    for i in range(n):
        row_is_zero = all(abs(matrix[i][j]) < eps for j in range(n))
        if row_is_zero:
            if abs(matrix[i][n]) > eps:
                raise ValueError("Układ sprzeczny (brak rozwiązań)")
            else:
                raise ValueError("Układ nieoznaczony (nieskończenie wiele rozwiązań)")

    x = back_solve(matrix)

    return x

#łączy macierz A z b i ją zwraca
def append_matrix(A, b):
    matrix = []
    for i in range(len(A)):
        matrix.append(A[i][:] + [b[i]]) # A[i][:] tworzy płytką kopię listy ?
    return matrix

#zwraca największą wartość w kolumnie k
def find_max(matrix, k):
    max_id = k
    for i in range(k, len(matrix)):
        if abs(matrix[i][k]) > abs(matrix[max_id][k]): #wartosc bezwzgledna, szukamy dominujacego elementu
            max_id = i
    return max_id

#zamienia wiersze
def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]

#zeruje elementy poniżej pivota
def eliminate_row(matrix, k):
    for i in range(k + 1, len(matrix)):
        multiplier = matrix[i][k] / matrix[k][k]
        for j in range(k, len(matrix[i])):
            matrix[i][j] -= multiplier * matrix[k][j]

#podstawianie wstecz
def back_solve(matrix):
    n = len(matrix)
    x = [0.0] * n
    for i in range(n - 1, -1, -1): #pętla od ostatniego wiersza do pierwszego
        sum1 = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (matrix[i][n] - sum1) / matrix[i][i]
    return x

#wyswietla macierz
def print_matrix(matrix):
    for row in matrix:
        print(row)