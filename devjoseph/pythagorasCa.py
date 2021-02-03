import math
# Formular for calculating Pythagoras Theorem is:
# a**2 + b**2 = c ** 2

# looking for the value of (C) when A and B is given

# Value of A
va_A = float(input("Please enter the value of a: "))
value_A = va_A ** 2
# Value of A is gotten

# Value of B
val_B = float(input("Please enter the value of b: "))
Value_B = val_B ** 2
# Value of B is gotten

# To get the value of C**2. we've to find sqaure root of both side
C = (value_A + Value_B)
CA = math.sqrt(C)

print(round(CA))