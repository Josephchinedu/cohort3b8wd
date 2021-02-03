import math
Question = input(" what equation are you looking to solve type \n  (Q) for quadratic equation or \n  (P) for pythagoras Theorem \n :  " )

if Question.upper() =="Q":
    print("for  ax^^+bx+c = 0 \n enter the parameters for (a), (b),(c)")
    a= int(input("Enter value for a : "))
    b= int(input("Enter value for b : "))
    c= int(input("Enter value for c : "))
    x1= (-b -((b**2) - (4*a*c))**0.5)/(2*a)
    x2= (-b +((b**2) - (4*a*c))**0.5)/(2*a)
    print(f"x={x1} or x={x2} ")

elif Question.upper() =="P":
    Q2 = input ("What parameters are you looking for \n (O)opposite, (A) Adjacent or (H) Hypothenus  :")

    if Q2.upper() =="O" :
        v1 = int (input("Enter Hypothenus: "))
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