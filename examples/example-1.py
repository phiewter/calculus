# Description: This script demonstrates examples of calculus in Python
# Created: 2025-01-13
# Modified: -

# Title: How to Do Calculus with Python?
# Source: https://www.geeksforgeeks.org/how-to-do-calculus-with-python/

# Importing library
import sympy as sp

# Declaring variables
x, y, z = sp.symbols('x y z')

# Expression of which we have to find the derivative of
expression = x**3 * y + y**3 + z

# Differentiating exp with respect to x
derivative1_x = sp.diff(expression, x)
print('derivative w.r.t. x: ', derivative1_x)

# Differentiating exp with respect to y
derivative1_y = sp.diff(expression, y)
print('derivative w.r.t. y:', derivative1_y)

# Finding the second derivative of exp with respect to x
derivative2_x = sp.diff(expression, x, 2)
print('second derivative w.r.t. x:', derivative2_x)

# Finding the second derivative of exp with respect to y
derivative2_y = sp.diff(expression, y, 2)
print('second derivative w.r.t. y:', derivative2_y)

# Indefinate integration of cos(x) w.r.t. dx
integral1 = sp.integrate(sp.cos(x), x)
print('indefinate integral of cos(x):', integral1)

# Definate integration of cos(x) w.r.t. dx between -1 to 1
integral2 = sp.integrate(sp.cos(x), (x, -1, 1))
print('definate integral of cos(x) between -1 to 1:', integral2)

# Definate integration of exp(-x) w.r.t. dx between 0 to ∞
integral3 = sp.integrate(sp.exp(-x), (x, 0, sp.oo))
print('definate integral of exp(-x) between 0 to ∞:', integral3)

# Calculating limit of f(x) = x as x->∞
limit1 = sp.limit(x, x, sp.oo)
print(limit1)

# Calculating limit of f(x) = 1/x as x->∞
limit2 = sp.limit(1/x, x, sp.oo)
print(limit2)

# Calculating limit of f(x) = sin(x)/x as x->0
limit3 = sp.limit(sp.sin(x)/x, x, 0)
print(limit3)

# Assign series
series1 = sp.series(sp.cos(x), x)
print(series1)

# Assign series
series2 = sp.series(1/sp.cos(x), x, 0, 4)
print(series2)