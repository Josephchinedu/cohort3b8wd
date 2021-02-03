# # def my_function(name):
# #     """ This function greets people """
# #     print("Hello Mr " + name + ", how are you today")
    
# # my_function("Joseph")

# def ano_function(num1, num2):
    
#     if type(num1) == type(num2) == type(4):
#         return num1 ** num2
#     else:
#         return "Sorry i want an integer"

# result = ano_function(4,2)
# print(result)
# print(ano_function.__doc__)

# Lambda function
# double = lambda x: x *2
# print(double(10))

my_list = [1,2,5,4,6,8,11,13,12]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)

m_list = [1,2,5,4,6,8,11,13,12]
new1_list = list(map(lambda x: x * 2, m_list))
print(new1_list)