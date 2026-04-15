import glob

from file_reader import read_matrix_from_file
from matrix_operations import check_diagonal_dominance

def print_equation(a, b):
    n = len(a)
    mid = n // 2

    for i in range(n):

        row = []
        for j in a[i]:
            number_in_row = f"{j:7g}"
            row.append(number_in_row)
        a_row = "  ".join(row)

        if i == mid:
            sign = " = "
        else:
            sign = "   "

        b_row = f"{b[i]:7g}"

        if n == 1:
            left, right = "[", "]"
        elif i == 0:
            left, right = "⎡", "⎤"
        elif i == n - 1:
            left, right = "⎣", "⎦"
        else:
            left, right = "⎢", "⎥"

        print(f"{left} {a_row} {right}  {left} x{i + 1} {right}{sign}{left} {b_row} {right}")

    if check_diagonal_dominance(a):
        diag_dom = "tak"
    else:
        diag_dom = "nie"

    print("\nSpełnia warunek dominacji przekątnej (gwarancja zbieżności dla metody iteracyjnej Gaussa-Seidla): " + diag_dom)

def print_all_equations():
    files = glob.glob("*.txt")
    files.sort()

    i = 0

    for filename in files:
        i += 1

        print("-" * 50)

        print(f"{i}. Przykład z pliku: {filename}\n")

        A, b = read_matrix_from_file(filename)

        print_equation(A, b)

    print("-" * 50)

    return files

def print_result(x):
    n = len(x)
    for i in range(n):
        print(f"x{i + 1} = {x[i]:7g}")

def print_error(error):
    print("Błąd wyniku: " + str(error))