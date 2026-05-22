from functions import horner_scheme

def compute_legendre_coefficients(degree: int) -> list[list[float]]:
    legendre_coeffs = [
        [1.0],
        [0.0, 1.0]
    ]

    for k in range(1, degree):
        # (k+1)P_{k+1}(x) = (2k+1)xP_k(x) - kP_{k-1}(x)

        # (2k+1) * x * P_k(x)
        shifted_coeffs = [0.0] + legendre_coeffs[k]
        multiplier = 2 * k + 1

        first_expression = []
        for i in range(len(shifted_coeffs)):
            first_expression.append(shifted_coeffs[i] * multiplier)

        # k * P_{k-1} * (x)
        second_expression = legendre_coeffs[k-1].copy()
        for i in range(len(second_expression)):
            second_expression[i] *= k

        # (2k+1) * x * P_k(x) - k * P_{k-1} * (x)
        numerator = []
        for i in range(len(first_expression)):
            if i < len(second_expression):
                numerator.append(first_expression[i] - second_expression[i])
            else:
                numerator.append(first_expression[i])

        # P_{k+1}(x) = ((2k+1) * x * P_k(x) - k * P_{k-1}(x)) / (k+1)
        denominator = k + 1
        next_poly_coeffs = []
        for val in numerator:
            next_poly_coeffs.append(val / denominator)

        legendre_coeffs.append(next_poly_coeffs)
    return legendre_coeffs

#polynomial_index - numer wielomianu (k=0 > p0(t), k=1 > p1(t), k=2 > p2(t))
#evalouation_point - punkt, w którym liczymy wartość wielomianu
def evaluate_legendre_polynomial(polynomial_index: int, evaluation_point: float, all_coeffs: list[list[float]]) -> float:
    coeffs = all_coeffs[polynomial_index]
    coeffs_reversed = coeffs[::-1]
    return horner_scheme(evaluation_point, coeffs_reversed)