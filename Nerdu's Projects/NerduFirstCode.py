print ("Welcome Nerdu!")
print ("Hello world")

print ("Welcome to my code.")

names = "Chinedu"


print (names)

a = 5

print ("Your access code is ", names,a)

filename="mydata.txt"
kere = "nerdubaby.csv"

with open(filename, "w") as file:
    file.write("Add this too. \n")

with open(filename, "r") as file:
    print(file.read())

with open(kere, "w") as file:
    print(file.write("one, two, three, \nfour, five, six"))

with open(kere, "a") as file:
    print(file.write("\nade, kunle, sunbo\n1,2,3"))

with open(kere, "r") as file:
        print(file.read())
