import numpy as np
import os
import matplotlib.pyplot as plt
from approximation import horner_scheme

def plot_approximation(function, function_approximated, error, start, end, n_nodes, filename=None):
    x_values = np.linspace(start, end, 200)

    y_original = [function(x) for x in x_values]

    combined_reversed = function_approximated[::-1]
    y_approximated = [horner_scheme((2 * x - start - end) / (end - start), combined_reversed) for x in x_values]

    plt.figure(figsize=(8, 5))

    plt.plot(x_values, y_original, label="Oryginalna")
    plt.plot(x_values, y_approximated, label="Wielomian aproksymacyjny")
    plt.grid(True)
    plt.xlim(start, end)
    plt.legend(loc='upper right')
    degree = len(function_approximated) - 1
    plt.title(f"stopień: {degree}, błąd: {error:.6f}")

    os.makedirs("plots", exist_ok=True)
    safe_error_str = str(round(error, 6)).replace(".", "_")
    filename = f"plot{degree}_nodes{n_nodes}_error_{safe_error_str}.png"
    filepath = os.path.join("plots", filename)
    plt.savefig(filepath, bbox_inches='tight')

    plt.show()