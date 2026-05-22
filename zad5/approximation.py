import math
from typing import Callable
from legendre import evaluate_legendre_polynomial
from gauss import gauss_legendre_integral
from legendre import compute_legendre_coefficients
from functions import horner_scheme

def compute_ck_coefficients(target_function: Callable[[float], float], start: float, end: float, k: int, n_nodes: int, all_legendre_coeffs: list[list[float]]) -> float:

    def integrand(x: float) -> float:
        # [a, b] -> [-1, 1]
        # t = (2x - a - b) / (b - a)
        t = (2 * x - start - end) / (end - start)
        return target_function(x) * evaluate_legendre_polynomial(k, t, all_legendre_coeffs)

    # int_{a}^{b} f(x) * P_k(t(x)) dx
    integral_result = gauss_legendre_integral(integrand, start, end, n_nodes)

    # c_k = ((2k + 1) / 2) * int_{a}^{b} f(x) * P_k(t(x)) dx
    c_k = ((2 * k + 1) / 2) * integral_result
    c_k *= 2 / (end-start)

    return c_k

def compute_approximation(target_function: Callable[[float], float], start: float, end: float, n_nodes: int, degree: int) -> list[float]:
    all_legendre_coeffs = compute_legendre_coefficients(degree)

    ck_coefficients = []
    for k in range(degree + 1):
        ck = compute_ck_coefficients(target_function, start, end, k, n_nodes, all_legendre_coeffs)
        ck_coefficients.append(ck)

    final_polynomial_coeffs = [0.0] * (degree+1)

    # F(x) = c_0*P_0(x) + c_1*P_1(x) + ... + c_m*P_m(x)
    for k in range(degree + 1):
        for i in range(len(all_legendre_coeffs[k])):
            final_polynomial_coeffs[i] += ck_coefficients[k] * all_legendre_coeffs[k][i]

    return final_polynomial_coeffs

def compute_error (target_function: Callable[[float], float], start: float, end: float, final_polynomial_coeffs: list[float], n_nodes) -> float:

    def integrand(x: float) -> float:
        # t = (2x - a - b) / (b - a)d
        t = (2 * x - start - end) / (end - start)
        combined_reversed = final_polynomial_coeffs[::-1]
        F_x = horner_scheme(t, combined_reversed)
        # (f(x) - F(x))^2
        return (target_function(x) - F_x)**2

    # int_{a}^{b} (f(x) - F(x))^2 dx
    gauss_error = gauss_legendre_integral(integrand, start, end, n_nodes)

    # sqrt(int_{a}^{b} (f(x) - F(x))^2 dx)
    return math.sqrt(gauss_error)