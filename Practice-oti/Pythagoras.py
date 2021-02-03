import math
Question = input("what Formula are you looking to solve  :")

Q2 = input ("What parameters are you looking for \n (O)opposite, (A) Adjacent or (H) Hypothenus  :")
if Q2.upper() =="O" :
    v1 = int(input("Enter Hypothenus: "))
    v2 = int(input("Enter Adjacent :"))
    while v1 > v2:
     Opposite = round (math.sqrt ((v1**2) - (v2**2)), 3)
     print(f"the opposite of the triangle is {Opposite}")
     break
    else:
        print("Invalid entry-hypothenus is always the longer side")

elif Q2.upper() =="A" :
    v3= int(input("Enter Hypothenus: "))
    v4= int(input("Enter Opposite :"))
    while v3 > v4 :
     adjacent = round (math.sqrt((v3**2) - (v4**2)) , 3)
     print(f"the Adjacent of the triangle is {adjacent}")
     break
    else:
        print("Invalid entry- Hypothenus is always the longer side")
        
elif Q2.upper() =="H" :
    v5= int(input("Enter Opposite: "))
    v6= int(input("Enter Adjacent :"))
    Hypothenus = round (math.sqrt ((v5**2) + (v6**2)) , 3)
    print(f"the opposite of the triangle is {Hypothenus}")

else:
    print("Invalid Input- Enter a valid parameter")
