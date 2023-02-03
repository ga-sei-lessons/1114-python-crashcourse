# # I am a comment, I will not be interpreted

# # I
# # am a
# # multiline comment

# '''
# I am a doc string, a special comment used to document 
# things like functions and modules
# '''

# """
# Three double quotes also make a doc string
# """

# # print is a 'built-in' funciton (part of the python standard library)
# # print("Hello, Spam!")

# # def = make a new function
# # def function_name(params):
# def compliment(name):
#     print("Nice Haircut,", name, "!")
#     # in function scope

# # out of function scope
# compliment("Theo")
# compliment("Gabe")

# # snake_case is how varaibles and functions are written
# # no keyword to define a variable
# my_varaible = "Daniel"
# compliment(my_varaible)
# my_varaible = "Emily"
# compliment(my_varaible)

# # no way to make a constant 'unchangable' var in python
# # just a naming convention
# MY_SCREAMING_CONST = "do not change me"
# # MY_SCREAMING_CONST = "what will happen?"

# # ## # ## # ## #
# # DATA TYPES

# # Booleans
# None # Nonetype is the abscence of a value (falsy), both undefine and null
# False # Explicitly falsy
# True # Explicity truthy

# # Strings (chars and text)
# 'single quotes are fine'
# "as are double quotes"

# # Numeric Datatypes
# # integers -- whole numbers
# 10
# 15
# -1
# 0
# # floating point numbers -- decimals
# 1.1
# 3.1415
# 10000.0000001
# # complex numbers
# 10j
# 13.5j

# # Data container types
# # these are reference types
# # lists = numerically indexed collection of items (aka an array)
# my_list = ['this', 'is', 'a', 'list of strings']
# not_a_copy = my_list # a reference to my_list

# # dictionaries
# # key/value pair stores
# my_dict = {
#     "key": "value",
#     10: "what",
#     True: "wtf python!"

# }

# print(my_dict)

# # checking the type in python
# print(type(my_list))
# print(type(11.1))

# # ## # ## # ## 
# # PYTHON CONTROL FLOW

# has_bank_account = False

# if has_bank_account:
#     # indent to scope code in the if
#     print("has bank account!")
# else:
#     print("does not have a bank account")

# # comparison and logical operators in python (class of operators that return bools)

# # comparisons
# # == - checks equality
# # != - checks inequality
# # > < >= <= - greater than/less than/is equal to

# # logical
# # and -- &&
# # or -- ||
# # not/! -- !

# account_balance = 97.55

# if has_bank_account and account_balance < 50:
#     print("you are broke!")
# elif has_bank_account and account_balance < 100:
#     print("you are seriously broke!")
# else:
#     print("all is well with the monies, or you have no account")

# # python ternaries (they are backwards)
# # [return value on true] if [condition] else [return value on false]
# should_get_account = "you do not need an account" if has_bank_account else "you should open an account"

# print(should_get_account)

# # ## # ## # ## 
# # String types

# breakfast = "spam eggs bacon sausage"
# # using dir (short for directory) to see all of the instance methods we can use
# # print(dir(breakfast))
# print(breakfast.upper()) # dot syntas to invoke object's instance methods
# print(breakfast.index('p'))
# # using bracket notation to access string indexes
# print(breakfast[1])
# # python has a len function to determin the length of things
# print(len(breakfast))
# # checking for a substring
# if "spam" in breakfast:
#     print("but I don't like spam!".upper())

# # string/list slicing syntax
# # [starting index : ending index : steps]
# # defaults: [0 : len(string) : 1]
# print(breakfast[:4])
# print(breakfast[5:])
# # make a copy of a string/list
# print(breakfast[:])

# # ## # ## #
# # Numbers and arithmitic

# # do math with python
# # + - / * % -- basic arihtmitic
# # += -= *= /= %= -- math + assigment operator
# # DOES NOT HAVE ++ or --
# my_num = 10
# my_num += 1
# print(my_num)
# # ** -- to the power of operator (also **=)
# print(2 ** 8) # 256
# # forced integer division // -- floors the result down to the nearest int
# print(15 // 2.5)

# ## # ## ## ## # 
# DATA CONTAINERS/ITERATION

# tuples are index lists that cannot change
my_tuple = ( 'cannot', 'change', 'values' )
# sets -- unindexed collections that must have unique values
my_set = { 'must', 'be', 'unique' }

my_list = ['spam', 'eggs', 'bacon', 'sausage']
my_dict = {
    'spam': 'eggs',
    'fruit': 'mango',
    'number': 10
}

# index of a list
print(my_list[0])
print(my_list[1:]) # remove the first item/keep everything after first item
new_list = my_list[:] # make a legit copy of the list
# print(dir([]))ß

my_list.append('spam') # adds to the end of the list
print(my_list)
my_list.insert(0, 'spam') # add a spam before the 0th index

# loop our list
# basic for loop works on both dicts lists
# for spam in my_list:
#     print(spam)

# for egg in my_dict:
#     # print(egg)
#     # print(my_dict[egg])
#     # format string/f string for short
#     print(f"key: {egg} value: {my_dict[egg]}")

# ennumerate function gets the index and value of a list
for i, item in enumerate(my_list):
    print(f'i: {i}, value: {item}')

# most similar to a 'for let i = 0' 
print(range(10)) # data type called a range
for i in range(10):
    # loop to 10
    print(i)

for i in range(len(my_list)): # evaluated once when the loop starts
    print(f'{i}: {my_list[i]}')

# while
i = 0
while i < len(my_list):
    print(f'while: {i}: {my_list[i]}')
    # advance i manually
    i += 1

# working with dictionary values
print(my_dict['spam'])
my_dict['spam'] = 'sausage'
my_dict['new_key'] = 'some value'
my_dict.pop('spam')
if 'spam' in my_dict:
    # skip this code if spam is not present
    my_dict.pop('spam')
print(my_dict)
# print(dir({}))