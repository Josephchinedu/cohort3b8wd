print(list(range(10)))

print(list(range(3,20)))

print(list(range(3,200,6)))

seq1 = [1, 2, 4, 5, 7]

print(list(reversed(seq1)))

seq2 = range(3, 27, 2)
print(list(reversed(seq2)))

c = (1, 2, 7, 3, 1, 6, 8, 4, 4, 6, 9)
print (sorted(c, reverse=True))

s = 22.7745
print(round(s, 3))

print (type(21))

print ("Your phone number is", "08085781217", sep = "\n")

from time import sleep
print ("Hi Nerdu.", end = " ", flush =True)
print ("Welcome to Python.")



q=[2,3,4,5,7,8]
print(sum(q, 10))

#Study print
#Most common: \t \n \r

name = input("Enter your name: ")
age = input("Please enter your age: ")
hobby1 = input("Please enter first hobby ")
hobby2 = input("Please enter second hobby: ")

print ("Loading", end = " ", flush = True)
sleep(.7)
print (".", end =" ", flush =True)
sleep(.7)
print (".", end =" ", flush =True)
sleep(.7)
print (".")
sleep (2)

print("\n", name.title(), "is", age, "years old. \nHobbies are listed below:")
print("\t-", hobby1)
print("\t-", hobby2)



