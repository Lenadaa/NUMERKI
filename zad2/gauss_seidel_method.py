from matrix_operations import append_matrix
MAX_ITERATIONS = 300

def gauss_seidel_method(A, b, stop_type, stop_accuracy):
    n = len(A)
    x = [0.0] * n  # wektor początkowy
    matrix = append_matrix(A, b)

    #iteracja
    if stop_type == 1:
        for iteration in range(stop_accuracy):
            for i in range(n):
                total = 0
                for j in range(n):
                    if j != i:
                        total += matrix[i][j] * x[j]
                x[i] = (matrix[i][n] - total) / matrix[i][i]
        return x, stop_accuracy

    #epsilon
    if stop_type == 2:
        iteration = 0
        while True:
            iteration += 1
            x_previous = x.copy()

            error = 0.0

            for i in range(n):
                total = 0
                for j in range(n):
                    if j != i:
                        total += matrix[i][j] * x[j]
                x[i] = (matrix[i][n] - total) / matrix[i][i]

            for i in range(n):
                curr_diff = abs(x[i] - x_previous[i])
                if curr_diff > error:
                    error = curr_diff

            if error < stop_accuracy:
                return x, iteration

            if iteration >= MAX_ITERATIONS:
                return x, iteration