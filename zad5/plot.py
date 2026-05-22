import numpy as np
import matplotlib.pyplot as plt
from approximation import horner_scheme

def plot_approximation(function, function_approximated, error, start, end, n_nodes):
    x_values = np.linspace(start, end, 200)

    y_original = [function(x) for x in x_values]

    combined_reversed = function_approximated[::-1]
    y_approximated = [horner_scheme((2 * x - start - end) / (end - start), combined_reversed) for x in x_values]

    plt.plot(x_values, y_original, label="Oryginalna")
    plt.plot(x_values, y_approximated, label="Wielomian aproksymacyjny")
    plt.legend()
    plt.grid(True)
    degree = len(function_approximated) - 1
    plt.title(f"Stopień: {degree}, błąd: {error:.6f}")

    plt.show()