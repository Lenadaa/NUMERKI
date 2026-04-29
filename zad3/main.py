import numpy as np
from functions import *
from interpolation import *
from file_io import *
from visualization import *
from test import *

def main():
    x_nodes = get_nodes()

    x_min, x_max = get_interpolation_interval()

    pipeline = build_composite_function()

    y_nodes = [composite(x, pipeline) for x in x_nodes]

    print("\n--- Wybór metody interpolacji ---")
    print("1. Metoda Lagrange'a")
    print("2. Metoda Newtona")
    method_choice = input("Wybierz (1-2): ")

    x_dense = np.linspace(x_min, x_max, 500)

    y_original = []
    y_interpolated = []

    if method_choice == '1':
        method_name = "Lagrange'a"
    if method_choice == '2':
        method_name = "Newtona"
        coeffs_newton = divided_differences(x_nodes, y_nodes)

    for x in x_dense:
        y_original.append(composite(x, pipeline))
        if method_choice == '2':
            y_interpolated.append(newton_interpolation(x, x_nodes, coeffs_newton))
        else:
            y_interpolated.append(lagrange_interpolation(x, x_nodes, y_nodes))

    plot_graph(x_nodes, y_nodes, x_dense.tolist(), y_original, y_interpolated,f"Metoda {method_name}")

def get_nodes() -> list[float]:
    print("--- Wczytywanie węzłów ---")
    while True:
        try:
            file_path = input("Podaj ścieżkę do pliku z węzłami: ")
            return load_nodes(file_path)
        except FileNotFoundError:
            print("Błąd: Podany plik nie istnieje.")
        except ValueError:
            print("Błąd: Plik zawiera nieprawidłowe dane.")

def select_function():
    while True:
        print("\nDostępne typy funkcji:")
        print("1. Liniowa (ax + b)")
        print("2. Bezwzględna (|x|)")
        print("3. Wielomian")
        print("4. Trygonometryczna (sin/cos/tan)")

        choice = input("Wybierz typ (1-4): ")

        if choice == '1':
            a = float(input("Podaj współczynnik a: "))
            b = float(input("Podaj współczynnik b: "))

            def wrapper(x):
                return linear_function(x, a, b)

            return wrapper

        elif choice == '2':
            def wrapper(x):
                return absolute_value_function(x)

            return wrapper

        elif choice == '3':
            count = int(input("Podaj ilość współczynników: "))
            coefficients = []
            degree = count - 1
            for i in range(count):
                coeff = float(input(f"Podaj współczynnik dla potęgi nr {degree}: "))
                coefficients.append(coeff)
                degree -= 1

            def wrapper(x):
                return polynomial_function(x, coefficients)

            return wrapper

        elif choice == '4':
            print("1. Sinus, 2. Cosinus, 3. Tangens")
            choice = input("Wybierz (1-3): ")
            choice_string = {'1': 'sin', '2': 'cos', '3': 'tan'}
            trig_type = choice_string.get(choice)

            def wrapper(x):
                return trigonometric_function(x, trig_type)

            return wrapper

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def build_composite_function() -> list:
    pipeline = []
    pipeline.append(select_function())

    while True:
        more = input("\nCzy chcesz dodać kolejną funkcję do złożenia? (y/n): ").lower()
        if more != 'y':
            break
        pipeline.append(select_function())

    return pipeline

def composite(x: float, pipeline: list) -> float:
    value = x
    for function in pipeline:
        value = function(value)
    return value

def get_interpolation_interval() -> tuple[float, float]:
    print("\n--- Podaj przedział ---")
    while True:
        try:
            a = float(input("Podaj początek: "))
            b = float(input("Podaj koniec: "))
            return a, b
        except ValueError:
            print("Błąd: Wprowadź poprawne liczby.")

if __name__ == "__main__":
    main()