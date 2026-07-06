import numpy as np
import sympy as sp
from scipy.interpolate import CubicSpline

x_vals = np.array([1, 2, 3, 4, 5, 6])
y_vals = np.array([1, 3, 5, 8, 5, 2])
x = sp.Symbol('x')

# 1. Lagrange Interpolation
lagrange_poly = 0
for i in range(len(x_vals)):
    term = y_vals[i]
    for j in range(len(x_vals)):
        if i != j:
            term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
    lagrange_poly += term
exact_lagrange = sp.expand(lagrange_poly)
print("Lagrange:", exact_lagrange)

# 2. Cubic Spline
cs = CubicSpline(x_vals, y_vals)
for i in range(len(x_vals) - 1):
    a, b, c, d = cs.c[:, i]
    xi = x_vals[i]
    spline_eq = a*(x - xi)**3 + b*(x - xi)**2 + c*(x - xi) + d
    print(f"Interval [{xi}, {x_vals[i+1]}]:", sp.expand(spline_eq))