from number_theory.modular_exponentiation import mod_exp
from number_theory.nth_magic_number import nth_magic_number

x = 2
y = 3
p = 5

print(mod_exp(x, y, p))

x = 2
y = 5
p = 13

print(mod_exp(x, y, p))

print(nth_magic_number(5))
