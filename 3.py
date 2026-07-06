import numpy as np
from scipy.integrate import trapezoid, simpson, fixed_quad, quad

def f(x): return np.exp(x**2)
a, b = 0, 1
x_vals = np.linspace(a, b, 101)
y_vals = f(x_vals)

print("Trapezoidal:", trapezoid(y_vals, x_vals))
print("Simpson's:", simpson(y_vals, x=x_vals))
integral_gauss, _ = fixed_quad(f, a, b, n=5)
print("Gaussian:", integral_gauss)
integral_exact, abs_error = quad(f, a, b)
print("Reference:", integral_exact)