from functions import *
from simpson import *
from gauss import *

def main():
    pipeline_list = build_composite_function()
    final_function = composition_function(pipeline_list)

    start, end = get_interval()
    epsilon = get_epsilon()

    simpson_result, simpson_iterations, simpson_n, simpson_evals = simpson_integral(final_function, start, end, epsilon)

    gauss_results = []
    for n in [2, 3, 4, 5]:
        gauss_results.append(gauss_legendre_integral(final_function, start, end, n))

    print_results(simpson_result, simpson_iterations, simpson_n, simpson_evals, gauss_results)

def print_results(simpson_result: float, simpson_iterations: int, simpson_n: int, simpson_evals: int, gauss_results: list[float]):
    print("\n" + "=" * 40)
    print("\n----- METODA SIMPSONA -----")
    print(f"Wynik:                      {simpson_result}")
    print(f"Liczba iteracji:            {simpson_iterations}")
    print(f"Liczba podprzedziałów:      {simpson_n}")
    print(f"Liczba wywołań:             {simpson_evals}")

    print("\n----- METODA GAUSSA-LEGENDRE'A -----")
    for idx, n_nodes in enumerate([2, 3, 4, 5]):
        result = gauss_results[idx]
        print(f"\nDla {n_nodes} węzłów:")
        print(f"  Wynik:                    {result}")
        print(f"  Liczba wywołań:           {n_nodes}")
    print("\n" + "=" * 40)

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

def get_epsilon():
    print("\nPodaj dokładność (epsilon).")
    epsilon = input("epsilon = ")
    return float(epsilon)

if __name__ == "__main__":
    main()