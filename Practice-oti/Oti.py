# name = input ("Enter name here:")
# age = input( "Enter age here:")
# hobby1 = input("Enter hobby here: ")
# hobby2 = input("Enter another hobby here: ")


# print("\n", "Hello ,", name, "I see that you are", age, "years old. \n", "And you seem to like the following below")
# print("\n","\t-", hobby2 )
# print("\t-", hobby1)

# Tripple = """ Ali is a young Adult, he works with a Multinantional 
# but he found his creative side in music and likes the genre Afropop.
#  One Day, he took the decision to address the Management on his intention to quit the organisation,
#     "But they Said, hey Ali, we know you have what is takes" """

# print(Tripple)


# word= input ("please enter a word")
# lower= word.upper()
# print(lower.endswith("Y"))

# number = input("Enter numbers here: ")|
# tr = int(number) % 2
# print("this's an odd number (true) or (false): ", bool(tr))

# number = input("Enter numbers here: ")
# print(not bool(int(number)%2))
# message = str(number) + " is an even number : " + str(not bool(int(number)%2))
# print(message)

# Name = input("enter name here")
# # Salary= input("enter salary here")
# January_Salary = 20000
# Frebruary_Salary= 50000
# March_Salary= 50000
# April_Salary= 50000
# May_Salary= 75000
# June_Salary= 50000
# Total_months =[January_Salary,Frebruary_Salary,March_Salary,April_Salary,May_Salary,June_Salary]
# Count_of_payment = len(Total_months)
# All_payment = sum(Total_months)
# Average_Salary = int(All_payment)/ int(Count_of_payment)
# max_salary = max(Total_months)
# Loan_Oblg = 35000
# message = "Mr." + Name +  " recieves an average salary of " + str(Average_Salary) + "\nnaira within the past " + str(Count_of_payment) + " months"

# print(message)

name= input("Enter name")
Principal = input("Enter principal")
Rate = input("Enter Rate")
Time = input("Enter Time")
prt = int(Principal)* int(Rate)* int(Time)
# Simple_I= (int(Principal)* int(Rate)* int(Time))/100
Simple_I= prt/100
# print(Simple_I)

# message = "Dear" + name + " if you take a loan of" + str(Principal) + "naira, at the rate of" + str(Rate) + "%, \nfor " + str(Time) + "months, you will pay back " + str(Simple_I) + " as interest. \nKindly click the button below to accept the terms and conditions"
message = f"Dear {name}  if you take a loan of{int(Principal):,} naira, at the rate of  {Rate}  %, \nfor {Time} months, you will pay back {Simple_I:,} as interest. \nKindly click the button below to accept the terms and conditions"
print(message)

# principal = input("Enter principal")
# rate = input("Enter Rate")
# time = input("enter duration")
# prt = principal*rate*time
# print(prt)



