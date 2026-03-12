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
        y_range = [functions.trigonometric(coeff[0],x) for x in x_range]
        ax.plot(x_range, y_range, label="h(x) Trygonometryczna")
        ax.scatter(bisectionValues[0], 0, color='blue')
        ax.scatter(secantValues[0], 0, color='red')
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
    elif type == 4:
        # Obliczamy y dla funkcji złożonej (coeff to tutaj nasza lista operations)
        y_range = [functions.complexFunction(coeff, val) for val in x_range]
        ax.scatter(bisectionValues[0], 0, color='blue')
        ax.scatter(secantValues[0],0,color="red")
        ax.plot(x_range, y_range, label="f(x) Złożona", color='green')
    ax.set_title("Wizualizacja funkcji")
    ax.legend(handles=[colorBlue, colorRed])
    plt.grid(True)
    plt.show()


def selectStop(stop,a,b,type,coefficients,stopAccuracy):
    if stop == 1:
        stopAccuracy = int(stopAccuracy)
        bisectionValues = bisection_it(a,b,type,coefficients,stopAccuracy)
        sceantValues = secant_it(a,b,type,coefficients,stopAccuracy)
        return bisectionValues,sceantValues
    elif stop == 2:
        bisectionValues = bisection_stop(a,b,type,coefficients,stopAccuracy)
        sceantValues = secant_stop(a,b,type,coefficients,stopAccuracy)
        return bisectionValues,sceantValues
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
def printResults(bisection,sceant):
    print("========= Wyniki metody bisekcji =========")
    print(f"Miejsce zerowe {bisection[0]}")
    print(f"Liczba iteracji {bisection[1]}")
    print("========= Wyniki metody siecznych =========")
    print(f"Miejsce zerowe {sceant[0]}")
    print(f"Liczba iteracji {sceant[1]}")
def basicFunctions(a,b):
    options = {
        1: "f(x) - Wielomian",
        2: "g(x) - Wykładnicza",
        3: "h(x) - Trygonometryczna",
    }
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
                x = float(input(f"Podaj współczynnik nr {i + 1}: "))
                coefficiants.append(x)
            return functionType, coefficiants
        except ValueError:
            raise ValueError("[BŁĄD] Wprowadz cyfre!")
    if functionType == 2:
        try:
            coefficiants = []
            print("========== Podaj współczynniki ==========")
            for i in range(3):
                userInput = float(input(f"Podaj współczynnik {i + 1}: "))
                coefficiants.append(userInput)
            return functionType, coefficiants
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
            return functionType, trigType
        except ValueError:
            raise ValueError("[BŁĄD] Wprowadz cyfre!")

    # h(x) = sin(x)              (Typ 3, coeff 1)
    # g(x) = 2x^2 + 10           (Typ 1, coeff [2, 0, 10])
    # f(x) = 2^x * 1 + 0         (Typ 2, coeff [2, 1, 0])

def complexFunctions(a,b):
    depth = int(input("Podaj stopień złożenia funkcji"))
    operations = []
    for i in range(depth):
        functionType, coeff = basicFunctions(a,b)
        operations.append((functionType,coeff))
    stopType, stopAccuracy = stopMethod()
    bisectionValues,secantValues = selectStop(stopType, a, b, 4, operations, stopAccuracy)
    return bisectionValues,secantValues,operations

print("======== Podaj granice ========")
a, b = limits()
print("======== Rodzaj funkcji ========")
print ("1. Podstawowe funkcje \n2. Złożone funkcje")
try:
    type = int(input("Podaj typ funkcji: "))
except ValueError:
    raise ValueError("[BŁĄD] Wprowadz cyfre!")
if type == 1:
    functionType,coeff = basicFunctions(a,b)
    stopType, stopAccuracy = stopMethod()
    bisectionValues,secantValues = selectStop(stopType, a, b, functionType, coeff,stopAccuracy)
    printResults(bisectionValues,secantValues)
    plots(functionType,a,b,coeff,bisectionValues,secantValues)
elif type == 2:
    bisectionValues, secantValues,operations = complexFunctions(a,b)
    printResults(bisectionValues,secantValues)
    plots(4,a,b,operations,bisectionValues,secantValues)
else: print("Nie istnieje taki typ")