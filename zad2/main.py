from gaussian_elimination import gaussian_elimination
from gauss_seidel_method import gauss_seidel_method
from display import *

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
                A, b = read_matrix_from_file(filename)
                menu(filename, A, b)
            else:
                print("Wybrany przykład nie istnieje.")
        except ValueError:
            print("Błąd: podaj liczbę. Wybierz numer zadania lub wpisz 'q', aby wyjść: ")

def menu(filename, A, b):
    while True:
        print(f"Wybrany plik z równaniem: {filename}")
        print("1. Metoda eliminacji Gaussa")
        print("2. Metoda iteracyjna Gaussa-Seidla")

        method = input("Wybierz metodę lub wpisz 'q', aby wrócić do wyboru zadania: ")

        if method == 'q':
            return

        try:
            method = int(method)

            if method == 1:
                run_gaussian_elimination(A, b)
            elif method == 2:
                run_gauss_seidel(A, b)
            else:
                print("Wybrana opcja nie istnieje.")
        except ValueError:
            print("Błąd: podaj liczbę.")

def run_gaussian_elimination(A, b):
    try:
        x = gaussian_elimination(A, b)
        print("Rozwiązanie:")
        print_result(x)
    except ValueError as e:
        print(f"Rozwiązanie: {e}")


def run_gauss_seidel(A, b):
    while True:
        print("Wybierz warunek stopu:")
        print("1. Ilość iteracji")
        print("2. Dokładność (epsilon)")

        stop_type = input("Wybierz warunek stopu lub wpisz 'q', aby wrócić do wyboru metody: ")

        if stop_type == 'q':
            return

        try:
            stop_type = int(stop_type)
            if stop_type == 1:
                stop_accuracy = int(input("Podaj liczbę iteracji: "))
            elif stop_type == 2:
                stop_accuracy = float(input("Podaj wartość epsilon: "))
            else:
                print("Wybrana opcja nie istnieje.")
                return

            x, iterations = gauss_seidel_method(A, b, stop_type, stop_accuracy)
            print(f"Szukanie rozwiązania zakończono po {iterations} iteracjach.")
            print_result(x)

        except ValueError:
            print("Błąd: podaj liczbę.")

if __name__ == "__main__":
    main()
