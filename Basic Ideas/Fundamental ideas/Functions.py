# Functions -> Standalone Function || print(), Type()
        #-> Method of class || upper(), replace()
        #-> Operations (Magic methods) || + - / * == in or


# Functions / Methods
# Functions -> independent block of code -> function_name(int value)
# Methods -> Functions belong to objects or classes -> value.method_name()

text = "hi"
number = 10

print(text)
print(number)

print(type(text))
print(type(number))

print(len(text))
# print(len(number)) # This is not ok.

print(text.upper())
#number.upper() # NOT OK

print(number.bit_length()) #This is ok for int but not for string

age = 21
height = 5 * 12 * 2.54
name = "Turjo Sarkar Prince"
student = True
novalue = None

print(age,
      name,
      height,
      student,
      novalue)


