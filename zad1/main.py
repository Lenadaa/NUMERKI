import matplotlib
from matplotlib import pyplot as plt
import numpy as np
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

options = {
    1: "f(x) wielomian",
    2: "g(x) wykładnicza",
    3: "h(x) trygonmetryczna",
    4: "f(g(x)) złożona",
    5: "h(f(x)) złożona "
}
print("====================")
print("Podaj type funkcji")
for i in options:
    print(f"{i}. {options[i]}")
functionType = int(input("Wybierz: "))
print("====================")
print("Podaj przedziały")
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
print("====================")
if functionType == 1:
    # wielomian
    # a,b,wspolczynniki


