from functions import *
from approximation import compute_approximation, compute_error
from plot import plot_approximation

def main():
    print("Aproksymacja wielomianami Legendre'a")

    print("\nWybierz funkcję aproksymowaną.")
    pipeline_list = build_composite_function()
    final_function = composition_function(pipeline_list)

    print("\nWybierz przedział.")
    start, end = get_interval()

    n_nodes = int(input("Podaj liczbę węzłów: "))

    print("\nWybierz tryb pracy")
    print("1. Tryb standardowy - podajesz stopień wielomianu")
    print("2. Tryb zaawansowany - podajesz oczekiwany błąd.")

    choice = input("Wybierz typ (1-2): ")

    if choice == '1':
        run_standard_mode(final_function, start, end, n_nodes)
    if choice == '2':
        run_advanced_mode(final_function, start, end, n_nodes)


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

            return linear_function(a, b)

        elif choice == '2':

            return absolute_value_function()

        elif choice == '3':
            count = int(input("Podaj ilość współczynników: "))
            coefficients = []
            degree = count - 1
            for i in range(count):
                coeff = float(input(f"Podaj współczynnik dla potęgi nr {degree}: "))
                coefficients.append(coeff)
                degree -= 1

            return polynomial_function(coefficients)

        elif choice == '4':
            print("1. Sinus, 2. Cosinus, 3. Tangens")
            choice = input("Wybierz (1-3): ")
            choice_string = {'1': 'sin', '2': 'cos', '3': 'tan'}
            trig_type = choice_string.get(choice)

            return trigonometric_function(trig_type)

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def build_composite_function() -> list:
    pipeline = [select_function()]

    while True:
        more = input("\nCzy chcesz dodać kolejną funkcję do złożenia? (y/n): ").lower()
        if more != 'y':
            break
        pipeline.append(select_function())

    return pipeline

def get_interval():
    print("\nPodaj granice przedziału (liczba lub pi).")

    def is_pi(text: str) -> float:
        text = text.strip().lower()
        if text == 'pi':
            return math.pi
        elif text == '-pi':
            return -math.pi
        else:
            return float(text)

    start = input("a = ")
    end = input("b = ")

    return is_pi(start), is_pi(end)

def run_standard_mode(target_function: Callable[[float], float], start: float, end: float, n_nodes: int):
    degree = int(input("\nPodaj stopień wielomianu aproksymacyjnego: "))

    coeffs = compute_approximation(target_function, start, end, n_nodes, degree)
    error = compute_error(target_function, start, end, coeffs, n_nodes)

    plot_approximation(target_function, coeffs, error, start, end, n_nodes)

    error = round(error, 6)

    print(f"\nStopień n: {degree}")
    print(f"Błąd: {error}")

def run_advanced_mode(target_function: Callable[[float], float], start: float, end: float, n_nodes: int):
    target_error = float(input("\nPodaj maksymalny błąd aproksymacji: "))

    degree = 1
    MAX_DEGREE = 20

    while degree <= MAX_DEGREE:
        coeffs = compute_approximation(target_function, start, end, n_nodes, degree)
        error = compute_error(target_function, start, end, coeffs, n_nodes)

        if error <= target_error:
            print(f"\nStopień n: {degree}")
            print(f"Błąd: {error}")
            print(f"Ilość iteracji: {degree}")

            plot_approximation(target_function, coeffs, error, start, end, n_nodes)
            return
        degree += 1

    error = round(error, 6)

    print(f"\nStopień n: {degree}")
    print(f"Błąd: {error}")
    print(f"Ilość iteracji: {degree}")

    plot_approximation(target_function, coeffs, error, start, end, n_nodes)

    return

if __name__ == "__main__":
    main()