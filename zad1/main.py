import bisection

print("Typy funkcji:")
print("1 - wielomian")
type = int(input("Podaj funkcje: "))

x = input("1 - iteracja, 2 - dokładność: ")

print("Podaj przedział")
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

if x == "1":
    it = int(input("Podaj ilość iteracji: "))
    print(bisection.bisection_it(it, type, a, b))
if x == "2":
    eps = float(input("Podaj dokładność: "))
    print(bisection.bisection_stop(eps,type, a, b));