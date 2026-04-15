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

#sprawdzenie czy macierz jest przekątniowo dominujaca
#jesli tak - gwarancja dla metody iteracyjnej iz znajdzie rozwiazanie
def check_diagonal_dominance(A):
    n = len(A)
    for i in range(n):
        sum_row = 0.0
        for j in range(n):
            if j != i:
                sum_row += abs(A[i][j])
        if abs(A[i][i]) <= sum_row:
            return False
    return True

#odleglosc miedzy nowymi a starymi x-ami
def compute_distance(new, old, metric):
    n = len(new)
    diffs = []

    #liczy roznice dla kazdej zmiennej
    for i in range(n):
        diff = abs(new[i] - old[i])
        diffs.append(diff)

    #euklidesowa
    if metric == 1:
        square_sum = 0.0
        for d in diffs:
            square_sum += d ** 2 #kazda roznica podniesiona do kwadratu i dodana do sumy
        return square_sum ** 0.5 #pierwiastek sumy

    #manhattan
    elif metric == 2:
        diff_sum = 0.0
        for d in diffs:
            diff_sum += d #suma bledow
        return diff_sum

    #maksimum
    elif metric == 3:
        return max(diffs) #najwiekszy blad

    else:
        raise ValueError(f"Nieznana metryka: {metric}")