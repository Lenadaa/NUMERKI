import glob

from gaussian_elimination import gaussian_elimination
from input import read

def main():
    files = print_all_equations()

    while True:
        choice = input("Wybierz układ do rozwiązania lub wpisz 'q', aby wyjść: ")
        if choice == 'q':
            break

        try:
            choice = int(choice)

            if 1 <= choice <= len(files):
                filename = files[choice - 1]
                A, b = read(filename)

                try:
                    x = gaussian_elimination(A, b)
                    x_len = len(x)
                    print("Rozwiązanie:")
                    for i in range(x_len):
                        print(f"x{i + 1} = {x[i]:7g}")
                except ValueError as e:
                    print(f"Rozwiązanie: {e}")
            else:
                print("Podany przykład nie istnieje.")
        except ValueError:
            print("Nieprawidłowy znak. Wpisz numer zadania lub 'q', aby wyjść.")


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

def print_all_equations():
    files = glob.glob("*.txt")
    files.sort()

    i = 0

    for filename in files:
        i += 1

        print("-" * 50)

        print(f"{i}. Przykład z pliku: {filename}\n")

        A, b = read(filename)

        print_equation(A, b)

    print("-" * 50)

    return files

if __name__ == "__main__":
    main()
