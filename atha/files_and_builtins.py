# filename ="mydata.txt"
# excel ="wkbk.csv"

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

# with open(excel, "w") as file:
#     print(file.write("ade, kunle, sunbo\n1,2,3"))

# with open("wkbk.csv", "r") as file:
#     print(file.read())


# nums = [1,2,3,4,5]
# print(min(nums))
# print(max(nums))

# names = ["ade", "nu", "semiat"]
# print(max(names))

# c = [1,4,4,1,23,9]

# print(sorted(c, reverse=False))
# print(sorted(names, reverse=True, key = len))


# x = round(10.476, 2)
# print(x)

# num = "23.432" # STRING REPRESENTATION OF A DECIMAL NUMBER
# num2 = 25.4321 # AN ACTUAL FLOATING POINT NUMBER

# # print(num - num2) # this will fail because num1 is a number while num is a text 
# print(float(num) - num2) # this will work because num has been converted into a number using the float  method

# print(type(54)) # tells you the type of any object

# name = "alimosho" # string

# print(name.upper()) # return upper case of string
# print(name.title()) # return capitalized first character.

# c = [1,4,4,1,23,9]
# name = "alimosho" # string

# print(len(name))
# print(len(c))

# Range function
# q = range(11) # giving range one parameter

# print(list(q))

# p = range(2, 11) # using 2 parameters (start and stop)
# print(list(p))

# r= range(2,11, 3) # using 3 parameters with the third being the steps to take

# print(list(r))

# r= range(1,-11, -3) # using 3 parameters with the third being the steps to take

# print(list(r))

# r= range(1,-11, 0) # using 3 parameters with the third being the steps to take

# print(list(r))

# my_list = [1,2,34,4,5,6,7,"we", "all"]

# print(list(reversed(my_list))) # reverses any list pased to it
# print(list(reversed(range(10))))

# print(1,2,3,4, end=" ")
# print(5,6,7,8, end="")

# print("joseph4", "jubilant@gmail.com")
# print("", "80332782", "22290823", sep = " +234-") # using the sep parameter to delimit the print values.

# from time import sleep

# # print("1")
# # sleep(2)
# # print("2")

# # print("1", end="") 
# # sleep(2)
# # print("2")

# print("1", end="", flush=True) 
# sleep(1)
# print("2", end="", flush=True)
# sleep(1)
# print("3", end="", flush=True)

# print("Alaba lo lo si aba lo ra shaba", file = open("alabashaba.txt", "w"))
# print("amazon depletio can cause global warming tipping point.", file = open("co2-warning.txt", "w")) # Using the file parameter you can use the print built in funtion to write to a file instead of streaming to default IO-stream.


# q= [2,3,4,5,7,8]

# print(sum(q))

# my_dict = {
#             "girl": "amaka",
#             "boy": "kunle"
#         } # CREATE SAMPLE DICTIONARY.

# print(my_dict)
# my_dict.pop("girl") # remove a key from a dictionary using the pop method, if item is not specified then the last value of the dict is removed by default..
# print(my_dict)
# print(54453656.0E50)

# x = "I'm a boy"
# x = "I\"m a boy'"
# print(x)

# text = "My matric number is 12\\ntd\\2021" # back slash can be used to silence any special character behaviours also

# print(text)

# print("ali \
# sunbo \
# kunle")

# print("Sobreiety", 
#         "Decimation", 
#         "interaction", 
#         "sublimation", 
#         "confirmation", 
#         "speculation")

# name = input("Please enter your name : ")
# age = input("Please enter your age : ")
# hobby1 = input("Please enter hobby : ")
# hobby2 = input("Please enter another hobby : ")

# # print(name)
# # print(age)
# # print(hobby1)
# # print(hobby2)

# print("\n", name.title(), "is", age, "years old. \nHobbies are listed below.")
# print("\t-", hobby1)
# print("\t-", hobby2)


# MAKING A STRING WITH ESCAPE CHARACTERS DISPLAY RAW WITHOUT IMPLEMENTING THE ESCAPE SEQUENCES USING THE R OR r PREFIX
# my_text = r"\nAlamu gave 3things, \nThese 3 things as listed below. \n\n\t1. Mangoes\n\t2. Oranges\n\t3. Apples"
# print(my_text)

# TRIPPLE QUOTED STRINGS
# THIS ALLOWS YOU THE FLEXIBILITY TO WRITE NORMALLY WITH EVERY KEYBOARD FORMATTING AND ON MULTIPLE LINES.

# drama = """Ali is a good boy, he sings afro beat and likes to experiment.
# One day, ali went to the board of directors,

# This is what he said,

# "I think im ready to take over the company".

#             Regards.
#             Alaba,
#             Story for the gods.
#                         """

# print(drama)

#BOOLEANS DATATYPE AND BOOL CONVERSION BUILTIN FUNCTION
# import time

# print(bool(1)) 
# time.sleep(1)
# print(bool(2)) 
# time.sleep(1)
# print(bool("ade")) 
# time.sleep(1)
# print(bool("s")) 
# time.sleep(1)
# print(bool(0)) 
# time.sleep(1)
# print(bool(-23)) 
# print(bool("")) 
# print(bool(" ")) 
# print(bool([])) 

# DIVMOD()

# print(divmod(20, 3))

# print(pow(4, 3))

# print(help(print))

# vals = [1,0]
# vals2 = [1,1]
# vals3 = [0,0]

# print("Vals", all(vals))
# print("Vals_2", all(vals2))
# print("Vals_3", all(vals3))
# print()
# print("Vals", any(vals))
# print("Vals_2", any(vals2))
# print("Vals_3", any(vals3))

# ENUMERATE

# names = ["ade", "kunle", "salami"]
# print(list(enumerate(names)))

# LOOP THROUGH EACH OF THE VALUES OF THE ENUMERATED LIST, SHOWING THE CORRESPONDING INDEX ASSIGNED DURING ENUMERATION.
# for index, name in enumerate(names):
#     print(index, "-> ", name)

# FILTER

# names = ["ade", "kunle", "salami", "ade", "shade", "ade"]

# print(list(filter(lambda name: name =="ade", names)))
# print(list(filter(lambda name: name=="ade", names)))

# MAP
names = ["ade", "kunle", "salami", "ade", "shade", "ade"]

x = map(lambda name: f"Dr. {name.title()}", names)
print(list(x))

x = map(lambda name: len(name), names)
print(list(x))

# F- STRING FORMAT. ALLOWS YOU TO LOAD A VARIABLE INTO A STRING TEMPLATE

# name = input("Please enter your name : ")
# age = input("Please enter your age : ")
# hobby1 = input("Please enter hobby : ")
# hobby2 = input("Please enter another hobby : ")

# message = f"{name} is a boy, who is only {age} years old, but can you imagine he likes to {hobby1} more than he even likes to {hobby2}."

# print(message)