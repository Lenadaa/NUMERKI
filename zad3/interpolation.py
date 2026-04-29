def lagrange_interpolation(x_target: float, x_nodes: list[float], y_nodes: list[float]) -> float:
    result = 0.0
    num_nodes = len(x_nodes)

    for i in range (num_nodes):
        basis = 1.0

        for j in range(num_nodes):
            if i != j:
                basis *= (x_target - x_nodes[j]) / (x_nodes[i] - x_nodes[j])

        result += basis * y_nodes[i]

    return result

def divided_differences(x_nodes: list[float], y_nodes: list[float]) -> list[float]:
    num_nodes = len(x_nodes)

    table = [[0.0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    for i in range(num_nodes):
        table[i][0] = y_nodes[i]

    for j in range(1, num_nodes):
        for i in range(num_nodes - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_nodes[i + j] - x_nodes[i])

    return table[0]

def newton_interpolation(x_target: float, x_nodes: list[float], coefficients: list[float]) -> float:
    result = coefficients[0]
    product = 1.0

    for i in range(1, len(coefficients)):
        product *= (x_target - x_nodes[i - 1])
        result += coefficients[i] * product

    return result