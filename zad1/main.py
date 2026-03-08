import matplotlib
from matplotlib import pyplot as plt
import bisection
import secant
import functions
import numpy as np


def plots(type,a,b):
    coloBlue = matplotlib.patches.Patch(color='blue', label='Metoda bisekcji')
    colorRed = matplotlib.patches.Patch(color='red', label='Metoda siecznych')
    fig, ax = plt.subplots(figsize=(8, 5))
    x_range = np.linspace(a, b, 50)
    if type == 1:
        y_range = [functions.polynomial(val) for val in x_range]
        ax.plot(x_range, y_range, label="Wielomian")
        ax.scatter(bisectionValues[0], 0, color='blue')
        ax.scatter(secantValues[0], 0, color='red')
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
    if type == 2:
        y_range = [functions.exponential(x) for x in x_range]
        ax.plot(x_range, y_range, label="Wykładnicza")
        ax.scatter(bisectionValues[0], 0, color='blue')
        ax.scatter(secantValues[0], 0, color='red')
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
    if type == 3:
        y_range = [functions.trigonometric(x) for x in x_range]
        ax.plot(x_range, y_range, label="Wykładnicza")
        ax.scatter(bisectionValues[0], 0, color='blue')
        ax.scatter(secantValues[0], 0, color='red')
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--')

    ax.set_title("Wizualizacja funkcji")
    ax.legend(handles=[coloBlue, colorRed])
    plt.grid(True)
    plt.show()

options = {
    1: "wielomian",
    2: "wykładnicza",
    3: "trygonmetryczna"
}

print("Typy funkcji:")
for i in options:
    print(i, options[i])
    x,a,b = 0,0,0
try:
    type = int(input("Podaj funkcje: \n"))
    x = int(input("1 - iteracja, 2 - dokładność: "))
    print("Podaj przedział")
    a = int(input("Podaj a: \n"))
    b = int(input("Podaj b: \n"))
except ValueError:
    print("Zła wartość")

if x == 1:
    try:
        it = int(input("Podaj ilość iteracji: "))
    except ValueError:
        print("Zła wartość")


    print("=== Metoda bisekcji ===")
    bisectionValues = bisection.bisection_it(it, type, a, b)
    print("Miejsce zerowe:")
    print(bisectionValues[0])
    print("Ilość iteracji:")
    print(bisectionValues[1])

    print("=== Metoda siecznych ===")
    secantValues = secant.secant_it(it, type, a, b)
    print("Miejsce zerowe:")
    print(secantValues[0])
    print("Ilość iteracji:")
    print(secantValues[1])

    plots(type,a,b)
if x == 2:
    try:
        eps = float(input("Podaj dokładność: "))
    except ValueError:
        print("Zła wartość")

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
    plots(type,a,b)