# Description: This script demonstrates examples of calculus in Python
# Created: 2025-01-13
# Modified: -

# Title: How to Do Calculus with Python?
# Source: https://www.geeksforgeeks.org/how-to-do-calculus-with-python/

# Importing library
import sympy as sym

# Declaring variables
x, y, z = sym.symbols('x y z')

# Expression of which we have to find the derivative of
expression = x**3 * y + y**3 + z

# Differentiating exp with respect to x
derivative1_x = sym.diff(expression, x)
print('derivative w.r.t. x: ', derivative1_x)

# Differentiating exp with respect to y
derivative1_y = sym.diff(expression, y)
print('derivative w.r.t. y:', derivative1_y)

# Finding the second derivative of exp with respect to x
derivative2_x = sym.diff(expression, x, 2)
print('second derivative w.r.t. x:', derivative2_x)

# Finding the second derivative of exp with respect to y
derivative2_y = sym.diff(expression, y, 2)
print('second derivative w.r.t. y:', derivative2_y)

# Indefinate integration of cos(x) w.r.t. dx
integral1 = sym.integrate(sym.cos(x), x)
print('indefinate integral of cos(x):', integral1)

# Definate integration of cos(x) w.r.t. dx between -1 to 1
integral2 = sym.integrate(sym.cos(x), (x, -1, 1))
print('definate integral of cos(x) between -1 to 1:', integral2)

# Definate integration of exp(-x) w.r.t. dx between 0 to ∞
integral3 = sym.integrate(sym.exp(-x), (x, 0, sym.oo))
print('definate integral of exp(-x) between 0 to ∞:', integral3)

# Calculating limit of f(x) = x as x->∞
limit1 = sym.limit(x, x, sym.oo)
print(limit1)

# Calculating limit of f(x) = 1/x as x->∞
limit2 = sym.limit(1/x, x, sym.oo)
print(limit2)

# Calculating limit of f(x) = sin(x)/x as x->0
limit3 = sym.limit(sym.sin(x)/x, x, 0)
print(limit3)

# Assign series
series1 = sym.series(sym.cos(x), x)
print(series1)

# Assign series
series2 = sym.series(1/sym.cos(x), x, 0, 4)
print(series2)