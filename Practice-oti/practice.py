# patient_name = "John Smith"
# patient_age = 20
# Status = "new"

# message = f"the patient's name is {patient_name} and he is {patient_age} old , he is a {Status} patient at the hospital"
# print(message)

# # has_good_credit = True
# # downp_good = 10
# # has_bad_credit = False
# # downp_bad = 20
# # if has_good_credit:
# #     print (f'You will need to put a down payment of {downp_good}%' )
# # elif has_bad_credit:
#     print  (f'You will need to put a down payment of {downp_bad}%' )
# weight =float( input ("Enter your weight :  "))
# unit = input ("L or Kg   ")

# if unit.upper ==("L"):
#     converted = weight * 0.45
#     print(f" you are {converted} kilos")

# else:
#     converted = weight//0.45
#     print(f"your weight is {converted} in pounds")
import math
Question = input("what Formula are you looking to solve  :")
Q2 = input ("(O)opposite, (A) Adjacent or (H) Hypothenus  :")
if Q2.upper() =="O" :
    v1 = int(input("Enter Hypothenus: "))
    v2 = int(input("Enter Adjacent :"))
    while v1 > v2:
     Opposite = math.sqrt ((v1**2) - (v2**2))
     print(f"the opposite of the triangle is {Opposite}")
    else:
        print("Invalid entry-hypothenus is always the longer side")

elif Q2.upper() =="A" :
    v3= int(input("Enter Hypothenus: "))
    v4= int(input("Enter Opposite :"))
    while v3 > v4 :
     adjacent = math.sqrt((v3**2) - (v4**2))
     print(f"the Adjacent of the triangle is {adjacent}")
    else:
        print("Invalid entry- Hypothenus is always the longer side")

elif Q2.upper() =="H" :
    v5= int(input("Enter Opposite: "))
    v6= int(input("Enter Adjacent :"))
    Hypothenus = math.sqrt ((v5**2) + (v6**2))
    print(f"the opposite of the triangle is {Hypothenus}")

else:
    print("Invalid Input")
