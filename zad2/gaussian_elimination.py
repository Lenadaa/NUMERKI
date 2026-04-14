from matrix_operations import append_matrix, find_max, swap_rows, eliminate_row, back_solve

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