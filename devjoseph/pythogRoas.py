import math
value_of_a = float(input("Enter the value of a: "))
VA = value_of_a ** 2

value_of_c = float(input("Enter the value of c: "))
VC = value_of_c ** 2

bT = VC - VA

# find the sqaure root "bT"

b = math.sqrt(bT)
print(round(b, 1))