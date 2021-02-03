c = 1

# def my_function():
#     c = c * 2
#     print(c)

# THIS FUNCTION FAILS BECAUSE WE ATTEMPT TO CHANGE A VARIABLE THAT DOES NOT EXIST I  SCPOPE
# my_function()


# print("This is the first print,. c = ", c)
# print("id c = ", id(c))

# def my_function():

#     c = 34
#     print("This is the first print,. c = ", c)
#     print("id c = ", id(c))

# my_function()
# print("This is the second print,. c = ", c)
# print("id c = ", id(c))

# ali = "boy"

# print("Is ali a boy - ", ali == "boy")
# print("Is ali a boy - ", not ali == "boy")
# import ada_namespace

# print(ada_namespace.name)
# print(ada_namespace.height)
# print(ada_namespace.age)

# list1 = ["junk", "important", "trash", "use", "important"]

# for item in list1:
#     if item == "important":
#         print("thats correct ")
#     else:
#         continue
#         print("Check next item")

# def do_something():
#     pass


# do_something()

# if True:
#     pass

# x = 1
# y = "sola"

# try:

#     print(x/y)

# except ZeroDivisionError:

#     print("Sorry you can not divide by zero")
# except TypeError:

#     print("Sorry you only int can divide int")
# finally:

#     print("Program completed")
    

# for char in "ABCDEF":
#     print(char)

# for value in [1,2,3,4,7,8,3,2]:
#     print(value,"-->", value *2)

# from ada_namespace import *

# # print(age)
# if age < 13:
#     print("sorry you are too young")
# else:
#     print(age)

# sequence = [1,2,3,4,7,8,3,2]
# print(10 in sequence)

# c = 20 # GLOBAL C

# def main():
#     c = 30 # nonlocal variable c
#     print(c)

#     def secondary():
#         nonlocal c
#         c = 40
#         print(c)

#     secondary()
#     print(c)

# main()
# print(c)

# i = 5

# while i:
#     print(i)
#     i = i-1

# print(bool(0))

age = 1500

if age > 10 and age < 18:
    print("You are an adolecent")
elif age > 17 and age < 40:
    print("you are an adult")
elif age > 40 and age < 190:
    print("You are an elder..")
elif age> 190 and age < 1200:
    print("You are an ancestor.")
else:
    print("Sorry your age is off the charts..")