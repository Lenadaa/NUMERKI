from matrix_operations import append_matrix, compute_distance, find_max
from zad2.matrix_operations import swap_rows

MAX_ITERATIONS = 50

def gauss_seidel_method(A, b, stop_type, stop_accuracy, metric_type):
    n = len(A)
    x = [0.0] * n  # wektor początkowy
    matrix = append_matrix(A, b)
    eps = 1e-10

    for k in range(n):
        max_id = find_max(matrix, k)
        if max_id != k:
            swap_rows(matrix, max_id, k)

        if abs(matrix[k][k]) < eps:
            raise ValueError("Macierz posiada zera na przekątnej.")

    #iteracja
    if stop_type == 1:
        for iteration in range(1, stop_accuracy + 1):
            x_previous = x.copy()
            for i in range(n):
                total = 0
                for j in range(n):
                    if j != i:
                        total += matrix[i][j] * x[j]
                x[i] = (matrix[i][n] - total) / matrix[i][i]

            error = compute_distance(x, x_previous, metric_type)


    #epsilon
    if stop_type == 2:
        iteration = 0
        while True:
            iteration += 1
            x_previous = x.copy()

            for i in range(n):
                total = 0
                for j in range(n):
                    if j != i:
                        total += matrix[i][j] * x[j]
                x[i] = (matrix[i][n] - total) / matrix[i][i]

            error = compute_distance(x, x_previous, metric_type)

            if error < stop_accuracy:
                break

            if iteration >= MAX_ITERATIONS:
                break

    return x, iteration, error