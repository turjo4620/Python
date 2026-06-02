# Create lists
empty = []
print(empty) # []
print(type(empty)) # <class 'list'>

# initialization
letters = ['a', 'b', 'c']
print(letters) # ['a', 'b', 'c']
print(type(letters)) # <class 'list'>

# list is just like a pointer, which is basically bearing the address and pointing to the actual data

numbers = [1, 2, 3]
print(numbers) # [1, 2, 3]
print(type(numbers)) # <class 'list'>

mixed = [1, 2, 3, 'a', 'b']
print(mixed) # [1, 2, 3, 'a', 'b']
print(type(mixed)) # <class 'list'>

# list(value) -> converts an iterable into a list 
letters = list('python')
print(letters) # ['p', 'y', 't', 'h', 'o', 'n']

# using range
numbers = list(range(5))
print(numbers) # [0, 1, 2, 3, 4]


# Access and Read

letters = ['a', 'b', 'c']

print(letters[0]) # first item
print(letters[-1]) # last item 

# slicing -> letters[ start : end + 1]
print(letters[0 : 3])

# if start from the first item then 
print(letters[ : 3])

# all the items
print(letters[ : ])

# unpacking

person = ['Turjo', 21, 'BUET-CSE']

# This is annoying!
# name = person[0]
# age = person[1]
# status = person[2]

name, age, status = person 

print(name)
print(age)
print(status)



