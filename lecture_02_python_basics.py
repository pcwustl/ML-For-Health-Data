# assign values to a variable
x = 3

# print the value of x
print(x)

# assign multiple values to multple variables
a, b = 3, 5
print(a)
print(b)

# return the type of the variable x
type(x)

# show documentation for the print() function
help(print)

"""## Strings"""

# assign a string to a variable
s1 = 'hello'

# Assign a multi-line string to the variable. 
# """ is also used to create strings that contain both " and ' characters
s2 = """She said,
"That's a good idea."
"""
print(s2)

# return the number of characters in a string
 len(s2)

# test whether the string starts with the substring "hel"
s1.startswith('hel')

# test whether the string ends with the substring "lo"
s1.endswith('ow')

# find a substring in a string
s1.find('he')
print('\n')
s1.find('He')

# return a string with the values 3, 1, and 4 inserted
"{} plus {} is {}".format(3, 1, 4)

# return a new string with all occurances of "e" replaced with "z"
s1.replace('e', 'E')

# split the string into a list of strings, 
# separating on the character " " (space) and return that list
s3 = 'I like drinking tea'
s3.split(' ')

# common string operations
my_string = 'this'
print(my_string * 2)
print(my_string + ' hat')
print('o' in my_string)

# common string methods
print(my_string.upper()) # turn to upper case
print(my_string.lower()) # turn to lower case
print(my_string.count('t')) # count the number of character 't'

# removes any leading (at the beginning) and trailing (at the end) space
apple = ' apple '
apple.strip()

"""## Numeric types and math operations"""

# convert the string "5" to the integer 5 and assign the result to i
i = int('5')
i

# convert the string "2.5" to the float value 2.5 and assign the result to f
f = float('2.5')
f

# raise 3 to the power of 2
3 ** 2

# 55           ÷          9           =         6           and         1
# dividend             divisor               quotient               remainder
print(55 / 9) # division
print(55 // 9) # quotient
print(55 % 9) # remainder

# assign the value of x + 1 to x
x = 5
x += 1
x

# assign the value of x - 1 to x
x = 5
x -= 1
x

"""## Lists"""

# assign a list containing the integers 100, 21, 88, and 3 to the variable l
l = [100, 21, 88, 3]
l

# create an empty list and assign the result to l
l = list() # option 1
l = [] # option 2
l

# return the first/last value in the list l
l = [100, 21, 88, 3]
print(l[0]) # first value
print(l[-1]) # last value

# return a slice of a list containing the second and third values of l 
# (excluding position 3)
print(l[1:3])

# more slice examples for list
print(l[:2]) # positions 0 and 1
print(l[1:]) # positions 1 to the end of the list
print(l[:]) # all positions

# subset list of a list
l1 = [[1, 2, -7, 8], [2, 3, 4], [-4, 9]]
print(l1[1][2])
print(l1[0][:2])

# list operations
my_list = ['this', 'is', 'nice']
print(my_list + l) # append list
print(my_list * 2) # duplicate elements in a list

# return the number of elements in l
len(l)

# return the sum, min, and max of element of l
print(sum(l))
print(min(l))
print(max(l))

# append the value 16 to the end of l
l.append(16)
print(l)

# get the index of an item in a list
print(my_list)
print(my_list.index('this'))

# count an item in a list
print(my_list.count('is'))

# remove an item from a list
l = [1, 2, 2, 5, 19, 20]
l.remove(2) # option 1: remove by value (only the first instance)
print(l)
del(l[1]) # option 2: remove by position
print(l)
print(l.pop(-1)) # option 3: remove by position and return the value removed
print(l)

# use list comprehension to remove all instances
l = [1, 2, 2, 5, 19, 20]
l_no_twos = [i for i in l if i != 2]
print(l_no_twos)

# reverse a list
l = [1, 2, 5, 19, 20]
l.reverse()
print(l)

# insert an item in a list by position
l.insert(1, -10)
print(l)

# sort items in l in ascending order
l2 = sorted(l) # option 1: make no change to the original list l
print(l2)
print(l)
l.sort() # option 2: make change to the original list l
print(l)

# sort items in l in descending order
l = [1, 2, 5, 19, 20]
print(sorted(l, reverse = True))

# convert the list ['A', 'B', 'C', 'D'] into the string "A B C D" 
# (with space in-between)
' '.join(['A', 'B', 'C', 'D'])

# tuple (= immutable list) and zip function
a = ('John', 'Charles', 'Mike')
b = (53, 29, 44)
x = zip(a, b)
list(x)

"""## List comprehension"""

# construct a new list with selected items from the original list
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []
for x in fruits:
  if 'a' in x:
    newlist.append(x)
print(newlist)

# use list comprehension to do the above task 
# newlist = [expression for item in iterable if condition == True]
newlist = [i for i in fruits if 'a' in i]
print(newlist)

"""## Dictionaries"""

# create a dictionary with keys of 'CA', 'GB', and 'IN' and 
# corresponding values of 'Canada', 'Great Britain', and 'India'
d = {'CA': 'Canada', 'GB': 'Great Britain', 'IN': 'India'}
print(d)

# return the value from the dictionary d that has the key 'GB'
d['GB']

# return the value from the dictionary d that has the key "AU"/"CA", 
# or the string "Sorry" if the key "AU"/"CA" is not found in d
print(d.get('AU', 'Sorry'))
print(d.get('CA', 'Sorry'))

# return a list of the keys from d
d.keys()

# return a list of the values from d
d.values()

# return a list of (key, value) pairs from d
d.items()

# create a loop to go through (key, value) pairs in d
for key, value in d.items():
  print(key)

"""## Modules and functions"""

# import the module random
import random

# import the function sqrt from the module math
from math import sqrt

# define a new function with two required and one optional arguments that 
# calculates and returns result
def calculate(value_one, value_two, exponent = 1):
  result = (value_one + value_two) ** exponent
  return result
print(calculate(2, 1))
print(calculate(2, 1, 2))

# use *args and **kwargs as an argument when we have an arbitrary number of 
# arguments we want to pass to a function
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))

# *args with first extra argument
def myFun(arg1, *argv):
    print ('First argument :', arg1)
    for arg in argv:
        print('Next argument through *argv :', arg)

myFun('Hello', 'Welcome', 'to', 'Machine Learning')

# the special syntax **kwargs is used to pass a keyworded argument list
# one can think of **kwargs as being a dictionary that maps each keyword to 
# the value that we pass alongside it
def concatenate(**kwargs):
    result = ''
    # iterate over the kwargs dictionary (kwargs stands for keyword arguments)
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a = 'Real', b = 'Python', c = 'Is', d = 'Great', e = '!'))

# a one-line simple function
(lambda x: x ** 2)(5)

"""## Boolean comparisons"""

# assign x, name, l, and dic
x = 18
name = 'alfred'
l = [1, 2, 5, 19, 20]
dic = {'A': 1, 'B': 2, 'C': 3}

print(x == 5) # test whether x is equal to 5
print(x != 5) # test whether x is not equal to 5
print(x > 5) # test whether x is greater than 5
print(x < 5) # test whether x is less than 5
print(x >= 5) # test whether x is greater than or equal to 5
print(x <= 5) # test whether x is less than or equal to 5
print(x == 5 or name == 'alfred') # test whether x is equal to 5 or name is equal to "alfred"
print(x == 5 and name == 'alfred') # test whether x is equal to 5 and name is equal to "alfred"
print(5 in l) # check whether the value 5 exists in the list l
print('A' in dic) # check whether 'A' is a key in dic

"""## If statement and loops"""

# test the value of the variable x and run the code body based on the value
x = 3
if x > 5:
  print("{} is greater than five".format(x))
elif x < 0:
  print("{} is negative".format(x))
else:
  print("{} is between zero and five".format(x))

# iterate over each value in l, running the code in the body of the loop
for value in range(10):
  print(value)
for item in [1, 5, -2, -7, 10]:
  print(item)

# run the code in the body of the loop until the value of x is no longer less than 10
x = 2
while x < 10:
  x += 1
print(x)

# enumerate function
l = [44, 55, 66, 77, 88]
for index, value in enumerate(l):
  print(index, value)