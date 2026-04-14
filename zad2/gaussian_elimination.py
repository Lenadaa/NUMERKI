def gaussian_elimination(A, b):
    n = len(A)
    matrix = append_matrix(A, b)

    for k in range(n):



    return

def append_matrix(A, b):
    matrix = []
    for i in range(len(A)):
        matrix.append(A[i] + [b[i]])
    return matrix

def find_max(matrix, k):
    max = k
    for i in range(r, len(matrix)):
        if matrix[i]

def znajdz_maks_wiersz(M, k):
    maks_wiersz = k
        for i in range(k, len(M)):
            if abs(M[i][k]) > abs(M[maks_wiersz][k]):
               maks_wiersz = i
            return maks_wiersz


# #sprawdza w kolumnie i, ktory wiersz ma najwieksza wartosc i zwraca jego indeks
# def find_max(matrix):
#     column = [row[0] for row in matrix]
#     value = max(column)
#     return column.index(value)
#
# #zamienia wiersze
# def swap_rows(matrix, i, j):
#     matrix[i], matrix[j] = matrix[j], matrix[i]
#
#wyswietla macierz
def print_matrix(matrix):
    for row in matrix:
        print(row)