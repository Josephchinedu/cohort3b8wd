a = float(input ("Please input lenght of first side, a: "))
b = float(input ("Please input lenght of second side, b: "))

csquare = a**2 + b**2

import math

c = math.sqrt(csquare)

message = f"The Hypotenuse of the triangle is {c}."

print (message)