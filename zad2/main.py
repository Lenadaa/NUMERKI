from gaussian_elimination import gaussian_elimination, print_matrix, append_matrix
from input import matrix

A, b = matrix("matrix.txt")
Ab = append_matrix(A, b)

print_matrix(A)
print_matrix(b)
print_matrix(Ab)