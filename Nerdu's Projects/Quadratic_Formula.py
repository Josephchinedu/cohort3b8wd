a = float(input ("Please enter term 'a' of equation: "))
b = float(input ("Please enter term 'b' of equation: "))
c = float(input ("Please enter term 'c' of equation: "))


import math

discriminant = math.sqrt((b**2) - (4*a*c))


root1 = (0-b+discriminant)/(2*a)
root2 = (0-b-discriminant)/(2*a)

message = f"The roots of the equation are {root1} and {root2}"

print (message)

