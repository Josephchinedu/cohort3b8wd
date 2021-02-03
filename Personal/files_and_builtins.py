filename ="mydata.txt"
excel ="wkbk.csv"

# file = open("mydata.txt", "r")

# print(file.read())

# file.close()

# file = open("mydata.txt", "a+")

# file.write("\n\nThis is a new info which i forgot earlier.")
# file.close()

# file = open("mydata.txt", "w")
# file.write("OOOPS this file has now been cleared.")

# with open(filename, "a") as file:
#     file.write("bla bla bla")

# with open(filename, "r") as file:
#     print(file.read())

with open(excel, "w") as file:
    print(file.write("ade, kunle, sunbo\n1,2,3"))

with open("wkbk.csv", "r") as file:
    print(file.read())

