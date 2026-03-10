import math

def polynomial(coefficient, x):
    result = coefficient[0]
    for i in range(1,len(coefficient)):
        result = result * x + coefficient[i]
    return result

#
# def polynomialDeriv(x):
#     a = 0.5
#     b = -3
#     c = 5
#     resultx = 3 * a * (x ** 2) + 2 * b * (x ** 1) + c
#     return resultx
#
# def exponential(a, x):
#     resultx = a ** x
#     return resultx
#
# def exponentialDeriv(x):
#     a = 5
#     result = (a**x) * math.log(a)
#     return result
#
# def trigonometric(x,trigType):
#     if trigType == 1:
#         result = math.sin(x)
#         return result
#     elif trigType == 2:
#         result = math.cos(x)
#         return result
#     elif trigType == 3:
#         result = math.tan(x)
#         return result
#     else:
#         return None
#
# def trigonometricDeriv(x,trigType):
#     if trigType == 1:
#         result  = math.cos(x)
#         return result
#     elif trigType == 2:
#         result = -1 * math.sin(x)
#         return result
#     elif trigType == 3:
#         a = math.cos(x) * math.cos(x)
#         return 1/a
#     else:
#         return None
# def complex_exp_in_poly(x):
#     resultx = exponential(x)
#     return polynomial(resultx)
#
# def complex_exp_in_polyDeriv(x):
#     fX = exponential(x)
#     return polynomialDeriv(fX) * exponentialDeriv(x)
#
# def complex_poly_in_tryg(x):
#     resultx = polynomial(x)
#     return trigonometric(resultx)
#
# def complex_poly_in_trygDeriv(x):
#     fX = polynomial(x)
#     return trigonometricDeriv(fX) * polynomialDeriv(x)
#
# def validationBisection(resultx0,resultx1,x1,x2,x0):
#     if (resultx0 == 0):
#         return x0, x0
#     if (resultx1 * resultx0 < 0):
#         return x1, x0
#     else:
#         return x0, x2
#
# def functionType(type,x1,x2,deriv,coeff):
#     if deriv == False:
#         if type == 1:
#             resultx1 = polynomial(coeff,x1)
#             resultx2 = polynomial(coeff,x2)
#             return resultx1, resultx2
#         elif type == 2:
#             resultx1 = exponential(x1)
#             resultx2 = exponential(x2)
#             return resultx1, resultx2
#         elif type == 3:
#             resultx1 = trigonometric(x1)
#             resultx2 = trigonometric(x2)
#             return resultx1, resultx2
#         elif type == 4:
#             resultx1 = complex_exp_in_poly(x1)
#             resultx2 = complex_exp_in_poly(x2)
#             return resultx1, resultx2
#         elif type == 5:
#             resultx1 = complex_poly_in_tryg(x1)
#             resultx2 = complex_poly_in_tryg(x2)
#             return resultx1, resultx2
#     else:
#         if type == 1:
#             resultx1 = polynomialDeriv(x1)
#             resultx2 = polynomialDeriv(x2)
#             return resultx1, resultx2
#         elif type == 2:
#             resultx1 = exponentialDeriv(x1)
#             resultx2 = exponentialDeriv(x2)
#             return resultx1, resultx2
#         elif type == 3:
#             resultx1 = trigonometricDeriv(x1)
#             resultx2 = trigonometricDeriv(x2)
#             return resultx1, resultx2
#         elif type == 4:
#             resultx1 = complex_exp_in_polyDeriv(x1)
#             resultx2 = complex_exp_in_polyDeriv(x2)
#             return resultx1, resultx2
#         elif type == 5:
#             resultx1 = complex_poly_in_trygDeriv(x1)
#             resultx2 = complex_poly_in_trygDeriv(x2)
#             return resultx1, resultx2
#
def polynomial(coefficient, x):
    result = coefficient[0]
    for i in range(1,len(coefficient)):
        result = result * x + coefficient[i]
    return result
