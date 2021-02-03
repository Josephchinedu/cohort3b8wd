# Given the string:
s = 'django'

# use the indexing to print out the following:

# 'd'
print(s[0])

# 'o'
print(s[5])

# 'djan'
print(s[:4])

# 'jan'
print(s[1:4])

# 'go'

print(s[4:])



# Proble no 2
# Given this nested list:

I = [3,7, [1,4,'hello']]

reassign = I[2][2] = "goodbye"
print(reassign)

# Reassign hello to be Goodbye



#Problem no 3

# using keys and indexing grab the 'hello' keyword from the followind dictionaries:
d1 = {'simplekey':'hello'}
print(d1['simplekey'])


d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1': [{'next_key':['this is deep', ['hello']]}]}
print(d3['k1'][0]['next_key'][1][0])


#problem no 4

# use set to find the unique value of the list

mylist = [1,1,1,1,1,1,2,2,2,2,2,2,44,4,4,4,4,4,4,4]
print(set(mylist))


#Problems no 5

# you are given two variables

age = 4
name = 'joseph'

print(f"Hello my name is {name} and {age} i'm  years old")


#use the print format to print the following words
# Hello my name is joseph and i'm 4 years old
