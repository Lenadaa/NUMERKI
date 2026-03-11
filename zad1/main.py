import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

from bisection import bisection_it, bisection_stop
from secant import secant_it, secant_stop
import functions

def plots(type,a,b,coeff,bisectionValues,secantValues):
    colorBlue = patches.Patch(color='blue', label='Metoda bisekcji')
    colorRed = patches.Patch(color='red', label='Metoda siecznych')
    fig, ax = plt.subplots(figsize=(8, 5))
    x_range = np.linspace(a, b, 50)
    if type == 1:
        y_range = [functions.polynomial_horner(coeff,val) for val in x_range]
        ax.plot(x_range, y_range, label="f(x) Wielomian")
        ax.scatter(bisectionValues[0], 0, color='blue')
        ax.scatter(secantValues[0], 0, color='red')
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
    elif type == 2:
        y_range = [functions.exponential(coeff,x) for x in x_range]
        ax.plot(x_range, y_range, label="g(x) Wykładnicza")
        ax.scatter(bisectionValues[0], 0, color='blue')
        ax.scatter(secantValues[0], 0, color='red')
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
    elif type == 3:
        y_range = [functions.trigonometric(coeff,x) for x in x_range]
        ax.plot(x_range, y_range, label="h(x) Trygonometryczna")
        ax.scatter(bisectionValues[0], 0, color='blue')
        ax.scatter(secantValues[0], 0, color='red')
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--')

    ax.set_title("Wizualizacja funkcji")
    ax.legend(handles=[colorBlue, colorRed])
    plt.grid(True)
    plt.show()


def selectStop(stop,a,b,type,coefficients,stopAccuracy):
    if stop == 1:
        stopAccuracy = int(stopAccuracy)
        bisectionValues = bisection_it(a,b,type,coefficients,stopAccuracy)
        sceantValues = secant_it(a,b,type,coefficients,stopAccuracy)
        return bisectionValues, sceantValues
    elif stop == 2:
        bisectionValues = bisection_stop(a,b,type,coefficients,stopAccuracy)
        sceantValues = secant_stop(a,b,type,coefficients,stopAccuracy)
        return bisectionValues, sceantValues
    else:
        raise ValueError("[BŁĄD] Nie istnieje taki warunek stopu!")
def limits():
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    return a,b
def stopMethod():
    print("===========  Warunki stopu =========== ")
    print("1. Iteracje")
    print("2. Dokładność")
    stopType = int(input("Podaj typ warunek stopu:"))
    stopAccuracy = float(input("Podaj warunek stopu: "))
    return stopType, stopAccuracy

options = {
    1: "f(x) - Wielomian",
    2: "g(x) - Wykładnicza",
    3: "h(x) - Trygonometryczna",
    4: "Funkcja złożona",
}
functionType = 0
print("=========== Wybierz funkcje =========== ")
for option in options:
    print(f"{option}: {options[option]}")
try:
    functionType = int(input("Podaj typ funkcji: "))
except ValueError:
    raise ValueError("[BŁĄD] Wprowadz cyfre!")
print("======================================")
if functionType == 1:
    try:
        coefficiants = []
        coefficientsNumber = int(input("Podaj liczbe współczynników: "))
        for i in range(coefficientsNumber):
            x = float(input(f"Podaj współczynnik nr {i+1}: "))
            coefficiants.append(x)
        a, b = limits()
        stopType, stopAccuracy = stopMethod()
        bisection,secant = selectStop(stopType,a,b,functionType,coefficiants,stopAccuracy)
        print(bisection)
        print(secant)
        plots(functionType,a,b,coefficiants,bisection,secant)
    except ValueError:
        raise ValueError("[BŁĄD] Wprowadz cyfre!")
if functionType == 2:
    try:
        coefficiants = []
        print("========== Podaj współczynniki ==========")
        for i in range(3):
            userInput = float(input(f"Podaj współczynnik {i+1}: "))
            coefficiants.append(userInput)
        a, b = limits()
        stopType, stopAccuracy = stopMethod()
        bisection,secant = selectStop(stopType,a,b,functionType,coefficiants,stopAccuracy)
        print(bisection)
        print(secant)
        plots(functionType,a,b,coefficiants,bisection,secant)
    except ValueError:
        raise ValueError("[BŁĄD] Wprowadz cyfre!")
if functionType == 3:
    try:
        trigType = []
        print("======= Podaj funkcje trygonometryczna =======")
        print("1. Sinus")
        print("2. Cosinus")
        print("3. Tangents")
        userInput = int(input("Podaj trygonometryczna (1,2,3): "))
        trigType.append(userInput)
        a,b = limits()
        stopType, stopAccuracy = stopMethod()
        print(trigType[0])
        bisection,secant = selectStop(stopType,a,b,functionType,trigType,stopAccuracy)
        print(bisection)
        print(secant)
        plots(functionType,a,b,trigType[0],bisection,secant)
    except ValueError:
        raise ValueError("[BŁĄD] Wprowadz cyfre!")
#
#
# print("----------WIELOMIAN----------")
# coefficients = [0.5, -3, 5, 3]
# print(bisection_it(-2, 2, 1, coefficients, 100))
# print(bisection_stop(-2, 2, 1, coefficients, 0.00000000001))
# print(secant_it(-2, 2, 1, coefficients, 100))
# print(secant_stop(-2, 2, 1, coefficients, 0.00000000001))
#
# print("----------F. WYKŁADNICZA----------")
# coefficients = [2, 2, -4]
# print(bisection_it(-2, 2, 2, coefficients, 100))
# print(bisection_stop(-2, 2, 2, coefficients, 0.00000000001))
# print(secant_it(-2, 2, 2, coefficients, 100))
# print(secant_stop(-2, 2, 2, coefficients, 0.00000000001))
#
# print("----------SIN(X)----------")
# coefficients = [1]
# print(bisection_it(-1, 1, 3, coefficients, 100))
# print(bisection_stop(-1, 1, 3, coefficients, 0.00000000001))
# print(secant_it(-1, 1, 3, coefficients, 100))
# print(secant_stop(-1, 1, 3, coefficients, 0.00000000001))
#
# print("----------COS(X)----------")
# coefficients = [2]
# print(bisection_it(1, 2, 3, coefficients, 100))
# print(bisection_stop(1, 2, 3, coefficients, 0.00000000001))
# print(secant_it(1, 2, 3, coefficients, 100))
# print(secant_stop(1, 2, 3, coefficients, 0.00000000001))
#
# print("----------TAN(X)----------")
# coefficients = [3]
# print(bisection_it(2, 4, 3, coefficients, 100))
# print(bisection_stop(2, 4, 3, coefficients, 0.00000000001))
# print(secant_it(2, 4, 3, coefficients, 100))
# print(secant_stop(2, 4, 3, coefficients, 0.00000000001))
#
# def plots(type,a,b,coeff):
#     colorBlue = matplotlib.patches.Patch(color='blue', label='Metoda bisekcji')
#     colorRed = matplotlib.patches.Patch(color='red', label='Metoda siecznych')
#     fig, ax = plt.subplots(figsize=(8, 5))
#     x_range = np.linspace(a, b, 50)
#     if type == 1:
#         y_range = [functions.polynomial(coeff,val) for val in x_range]
#         ax.plot(x_range, y_range, label="f(x) Wielomian")
#         ax.scatter(bisectionValues[0], 0, color='blue')
#         # ax.scatter(secantValues[0], 0, color='red')
#         ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
#     if type == 2:
#         y_range = [functions.exponential(x) for x in x_range]
#         ax.plot(x_range, y_range, label="g(x) Wykładnicza")
#         ax.scatter(bisectionValues[0], 0, color='blue')
#         ax.scatter(secantValues[0], 0, color='red')
#         ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
#     if type == 3:
#         y_range = [functions.trigonometric(x) for x in x_range]
#         ax.plot(x_range, y_range, label="h(x) Trygonometryczna")
#         ax.scatter(bisectionValues[0], 0, color='blue')
#         ax.scatter(secantValues[0], 0, color='red')
#         ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
#     if type == 4:
#         y_range = [functions.complex_exp_in_poly(x) for x in x_range]
#         ax.plot(x_range, y_range, label="f(g(x)) Złożona")
#         ax.scatter(bisectionValues[0], 0, color='blue')
#         ax.scatter(secantValues[0], 0, color='red')
#         ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
#     if type == 5:
#         y_range = [functions.complex_poly_in_tryg(x) for x in x_range]
#         ax.plot(x_range, y_range, label="h(f(x)) Złożona")
#         ax.scatter(bisectionValues[0], 0, color='blue')
#         ax.scatter(secantValues[0], 0, color='red')
#         ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
#
#     ax.set_title("Wizualizacja funkcji")
#     ax.legend(handles=[colorBlue, colorRed])
#     plt.grid(True)
#     plt.show()
#
# options = {
#     1: "f(x) wielomian",
#     2: "g(x) wykładnicza",
#     3: "h(x) trygonmetryczna",
#     4: "f(g(x)) złożona",
#     5: "h(f(x)) złożona "
# }
#
# print("Typy funkcji:")
# for i in options:
#     print(i, options[i])
#     x,a,b = 0,0,0
# try:
#     type = int(input("Podaj funkcje: \n"))
#     if type==1:
#         coefficientsAmount = int(input("Podaj ilość współczynników: \n"))
#         coefficients = []
#         for j in range(coefficientsAmount):
#             userInput = float(input(f"Podaj współlczynnik nr {j}"))
#             coefficients.append(userInput)
#     elif type==3:
#         trigType = input("Wybierz funkcje trygonometryczna: \n 1. Sin \n 2.Cos  \n 3. Tan")
#
#     x = int(input("1 - iteracja, 2 - dokładność: "))
#     print("Podaj przedział")
#     a = int(input("Podaj a: \n"))
#     b = int(input("Podaj b: \n"))
# except ValueError:
#     print("Zła wartość")
#
# if x == 1:
#     try:
#         it = int(input("Podaj ilość iteracji: "))
#     except ValueError:
#         print("Zła wartość")
#
#
#     print("=== Metoda bisekcji ===")
#     bisectionValues = bisection.bisection_it(it, type, a, b,coefficients)
#     print("Miejsce zerowe:")
#     print(bisectionValues[0])
#     print("Ilość iteracji:")
#     print(bisectionValues[1])
#
#     # print("=== Metoda siecznych ===")
#     # secantValues = secant.secant_it(it, type, a, b)
#     # print("Miejsce zerowe:")
#     # print(secantValues[0])
#     # print("Ilość iteracji:")
#     # print(secantValues[1])
#     plots(type,a,b,coefficients)
# if x == 2:
#     try:
#         eps = float(input("Podaj dokładność: "))
#     except ValueError:
#         print("Zła wartość")
#
#     print("=== Metoda bisekcji ===")
#     bisectionValues = bisection.bisection_stop(eps, type, a, b,coefficients)
#     print("Miejsce zerowe:")
#     print(bisectionValues[0])
#     print("Ilość iteracji:")
#     print(bisectionValues[1])
#
#     print("=== Metoda siecznych ===")
#     secantValues = secant.secant_stop(eps, type, a, b)
#     print("Miejsce zerowe:")
#     print(secantValues[0])
#     print("Ilość iteracji:")
#     print(secantValues[1])
#     plots(type,a,b,coefficients)

# options = {
#     1: "f(x) wielomian",
#     2: "g(x) wykładnicza",
#     3: "h(x) trygonmetryczna",
#     4: "f(g(x)) złożona",
#     5: "h(f(x)) złożona "
# }
# print("====================")
# print("Podaj type funkcji")
# for i in options:
#     print(f"{i}. {options[i]}")
# functionType = int(input("Wybierz: "))
# print("====================")
# print("Podaj przedziały")
# a = float(input("Podaj a: "))
# b = float(input("Podaj b: "))
# print("====================")
# if functionType == 1:
#     # wielomian
#     # a,b,wspolczynniki
#
#
