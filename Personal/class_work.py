# print("Hello World!!!")
# print ("Davinchy on pyhton")
# print ("Courtesy Liberty Assured's Oristetimeyin Igbene")

# print("WELCOME TO CLASS TODAY AND CHECK IF A WORD STARTS WITH (A).")
# word=input("What is your name: ")
# print(word.startswith("a"))

# print("WELCOME TO CLASS TODAY AND CHECK IF YOUR NAME ENDS WITH (U).")
# word=input("WHAT IS YOUR NAME: ")
# normalize = word.lower()

# print(normalize.endswith("u"))

# print("This exercise is Checking out for True or False")
# age = input("What is your age? ")
# month =input("month of birth: ")
# result = int(age) + int(month)
# message = "Is " + str(result) + " a even number?: " + str(not bool(result%2))
# print(message)

# print("A program to calculaye Simple Interest")
# Principal = input("What loan amount do you want? ")
# Rate = input("What is the rate? ")
# Duration = input("For what duration? ")
# result1 = int(Principal) * int(Rate) * int(Duration)
# result2 = (result1)/(100)
# message = "If you take a loan of " + Principal + " at the rate of " + Rate + " for " + Duration + " months, you will pay back " + str(result2) + " as interest."
# print(message)  


print("A program to calculaye Simple Interest")
P = float(input("What loan amount do you want? "))
R = (float(input("What is the rate? ")))
D = (float(input("For what duration? ")))
r1 = (P) * (R) * (D)
r2 = (r1)/(100)
message = f"If you take a loan of {P:,} at the rate of {R}% for {D}months, you will pay back total of {r2:,} as monthly interest."
print(message)