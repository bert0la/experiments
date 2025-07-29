from sympy import symbols, integrate, ln

x = symbols('x', real=True)

f = 1/x

integral = integrate(f, x)
print("Integral de 1/x:", integral)
