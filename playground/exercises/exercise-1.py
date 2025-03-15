# Description:  Calculating speed and acceleration from distance
# Created:      2025-01-13
# Modified:     -

import sympy as sp

# Expression:   s(t) = 5*t**3 - 20*t**2 + 15*t

t = sp.symbols('t')
s = 5*t**3 - 20*t**2 + 15*t

# Exercise 1: Use 'SymPy' to:
#   Exercise 1.1: Differentiate s(t) to find velocity v(t) as a function of time
#   Exercise 1.2: Differentiate v(t) to find the acceleration a(t) as a function of time

v = sp.diff(s, t)
a = sp.diff(v, t)

print(v, a)

# Exercise 2: Evaluate the following:
#   Exercise 2.1: The car's velocity at t = 4 seconds
#   Exercise 2.2: The car's acceleration at t = 4 seconds

velocity_at_4 = v.subs(t, 4)
acceleration_at_4 = a.subs(t, 4)

print(velocity_at_4, acceleration_at_4)

# Exercise 3: Find the time t at which the velocity is zero

time_when_velocity_zero = sp.solve(v, t)

print(time_when_velocity_zero)

# Exercise 4: Bonus: Plot s(t), v(t), and a(t) using Matplotlib