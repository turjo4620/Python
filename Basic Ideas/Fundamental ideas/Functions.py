# # Functions -> Standalone Function || print(), Type()
#         #-> Method of class || upper(), replace()
#         #-> Operations (Magic methods) || + - / * == in or


# # Functions / Methods
# # Functions -> independent block of code -> function_name(int value)
# # Methods -> Functions belong to objects or classes -> value.method_name()

# text = "hi"
# number = 10

# print(text)
# print(number)

# print(type(text))
# print(type(number))

# print(len(text))
# # print(len(number)) # This is not ok.

# print(text.upper())
# #number.upper() # NOT OK

# print(number.bit_length()) #This is ok for int but not for string

# age = 21
# height = 5 * 12 * 2.54
# name = "Turjo Sarkar Prince"
# student = True
# novalue = None

# print(age,
#       name,
#       height,
#       student,
#       novalue)



# User defined function

def greet(name):
    return f"Hello, {name}!!"

message = greet("Turjo")
print(message)

# Function parameters

def power(base, exponent = 2):
    return base **  exponent

print(power(3)) # default : 3 ^ 2 -> 9
print(power(3, 3)) # 3 ** 3

def introduce(name, age, city):
    return f"{name} is {age} years old and lives in {city}"


# print(introduce("Turjo", 21, "Sylhet"))
print(introduce(name = "Turjo", age = 21, city = "Sylhet"))


# Lambda Functions

square = lambda x : x ** 2

print(square(5)) # output : 25

# common use with map , filter

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x : x ** 2, numbers))
print(squared)

evens = list(filter(lambda x : x % 2 == 0, numbers))
print(evens)

from functools import reduce

product = reduce(lambda acc, x : acc * x, numbers, 1)
print(product)
# acc is the product accumulator and it's intial value is set to 1

