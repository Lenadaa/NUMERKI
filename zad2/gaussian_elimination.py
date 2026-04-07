def gaussian_elimination(matrix, n):
    index = find_max(matrix)
    if index != 0:
        swap_rows(matrix, 0, index)

    print_matrix(matrix)

#sprawdza w kolumnie i, ktory wiersz ma najwieksza wartosc i zwraca jego indeks
def find_max(matrix):
    column = [row[0] for row in matrix]
    value = max(column)
    return column.index(value)

#zamienia wiersze
def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]

#wyswietla macierz
def print_matrix(matrix):
    for row in matrix:
        print(row)