from gaussian_elimination import gaussian_elimination

matrix = [
    [2.0, 5.0, 7.0, 33.0],
    [3.0, 3.0, 3.1, 12.0],
    [1.0, 2.0, 1.0, 8.0]
]
n = 3

gaussian_elimination(matrix, n)