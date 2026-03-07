import bisection
import secant

print("Typy funkcji:")
print("1 - wielomian")
print("2 - wykładnicza")
print("3 - trygonometryczna")
type = int(input("Podaj funkcje: "))

x = input("1 - iteracja, 2 - dokładność: ")

print("Podaj przedział")
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

if x == "1":

    it = int(input("Podaj ilość iteracji: "))

    print("=== Metoda bisekcji ===")
    print("Miejsce zerowe:")
    print(bisection.bisection_it(it, type, a, b))

    print("=== Metoda siecznych ===")
    print("Miejsce zerowe:")
    print(secant.secant_it(it, type, a, b))

if x == "2":

    eps = float(input("Podaj dokładność: "))
    print(bisection.bisection_stop(eps,type, a, b))

    print("=== Metoda bisekcji ===")
    bisectionValues = bisection.bisection_stop(eps, type, a, b)
    print("Miejsce zerowe:")
    print(bisectionValues[0])
    print("Ilość iteracji:")
    print(bisectionValues[1])

    print("=== Metoda siecznych ===")
    secantValues = secant.secant_stop(eps, type, a, b)
    print("Miejsce zerowe:")
    print(secantValues[0])
    print("Ilość iteracji:")
    print(secantValues[1])
