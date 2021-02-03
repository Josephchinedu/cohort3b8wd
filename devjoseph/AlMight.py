import math 

# Use the almight formular to solve 

#forular is ax**2+bx+c=0

# = b+- squrt b**2 - 4ac / 2a

# let's look for the value of "a" from the user input
value_of_a = float(input("please enter the value of a: "))

# Value of multiply by (2a) 2
value_of_ai = value_of_a * 2

# let's look for the value of "b" from the user input
value_of_b = float(input("please enter the value of b: "))


# let's look for the value of "c" from the user input
value_of_c = float(input("please enter the value of c: "))

# We're looking for the value of "X"

# solving this part (b**2 4ac)
finding_X = ( value_of_b ** 2 - 4 * value_of_a * value_of_c)

square_rot = math.sqrt(finding_X)
print(square_rot)


# Now i'm solving -b +- sqaure of (finding_x) / value_of_ai positive side
# Now it should be -b + sqaure of (finding_x) / value_of_ai
anwser_for_positive_X = ( - value_of_b + square_rot) / value_of_ai
anwser_for_positive_Xf = round(anwser_for_positive_X, 2)
print(f"with almight formular i've solved this numbers, {value_of_a} {value_of_b} and {value_of_c} and \nhere's my (+) answer:  {anwser_for_positive_Xf}")

# # print()

# anwser_for_positive_Xf = (- value_of_b - math.sqrt(finding_X)) / value_of_ai
# anwser_for_positive_Xff = round(anwser_for_positive_Xf, 2)
# print(f"here's my (-) answer:  {anwser_for_positive_Xff}")





