import numpy as np
from functions import *
from interpolation import *
from file_io import *
from visualization import *
from main import *

def test(nodes, x_range, functions_list, title):
    x_min, x_max = x_range

    y_nodes = [composite(x, functions_list) for x in nodes]

    x_dense = np.linspace(x_min, x_max, 500)
    y_original = [composite(x, functions_list) for x in x_dense]

    coeffs_newton = divided_differences(nodes, y_nodes)
    y_newton = [newton_interpolation(x, nodes, coeffs_newton) for x in x_dense]

    plot_graph(nodes, y_nodes, x_dense.tolist(), y_original, y_newton, f"{title} - Newton")

    y_lagrange = [lagrange_interpolation(x, nodes, y_nodes) for x in x_dense]

    plot_graph(nodes, y_nodes, x_dense.tolist(), y_original, y_lagrange, f"{title} - Lagrange")


def test1():
    def linear_f(x): return linear_function(x, 2, 3)
    test([-5.2, -1.0, 4.8], (-6, 6), [linear_f], "Test 1: f(x) = 2x + 3")

def test2():
    def parabola_f(x): return polynomial_function(x, [1, 0, -4])
    test([-3.5, -0.5, 1.2, 3.8], (-4, 4), [parabola_f], "Test 2: f(x) = x^2 - 4")

def test3():
    def sin_f(x): return trigonometric_function(x, 'sin')
    test([-3.8, -2.1, 0.1, 1.5, 3.9], (-4, 4), [sin_f], "Test 3: f(x) = sin(x)")

def test4():
    def abs_f(x): return absolute_value_function(x)
    test([-4.5, -1.2, 0.0, 0.8, 4.2], (-5, 5), [abs_f], "Test 4: f(x) = |x|")

def test5():
    def sin_f(x): return trigonometric_function(x, 'sin')
    def abs_f(x): return absolute_value_function(x)
    test([-3.2, -1.8, 0.5, 1.2, 3.5], (-4, 4), [sin_f, abs_f], "Test 5: f(x) = |sin(x)|")

def test6():
    def abs_f(x): return absolute_value_function(x)
    def sin_f(x): return trigonometric_function(x, 'sin')
    test([-6.1, -2.5, 0.0, 1.1, 5.8], (-7, 7), [abs_f, sin_f], "Test 6: f(x) = sin(|x|)")

def test7():
    def cubic_f(x): return polynomial_function(x, [1, 0, -3, 0])
    test([-2.8, -0.8, 0.2, 2.5], (-3, 3), [cubic_f], "Test 7: f(x) = x^3 - 3x")

def test8():
    def tan_f(x): return trigonometric_function(x, 'tan')
    test([-1.2, -0.7, 0.1, 0.9, 1.3], (-1.4, 1.4), [tan_f], "Test 8: f(x) = tan(x)")

def test9():
    def poly_f(x): return polynomial_function(x, [1, 0, -2])
    def abs_f(x): return absolute_value_function(x)
    test([-2.9, -1.5, -0.2, 1.4, 2.7], (-3, 3), [poly_f, abs_f], "Test 9: f(x) = |x^2 - 2|")

def test10():
    def abs_f(x): return absolute_value_function(x)
    def lin_f(x): return linear_function(x, 1, -3)
    test([-5.5, -3.0, -1.1, 0.2, 3.0, 5.2], (-6, 6), [abs_f, lin_f, abs_f], "Test 10: f(x) = ||x| - 3|")