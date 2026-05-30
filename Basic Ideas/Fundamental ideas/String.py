
# type() and str()

name = "Turjo"

print(type(name))

age = 24
print(type(age))

# print("Your age is: " + age)
# this will not work because string + int is not valid

print("Your age is: " + str(age))

age = age + 5
# this is ok!


# len() and count()

password = "123a"
print(len(password))

if(len(password) < 8):
    print("Your password is too short!")


text = """
Python is very easy to learn.
Python is powerful.
"""
print(text.count("Python")) # case sensitive



# Transformations

# replace()

date1 = "20/05/2025"
print(date1.replace("/", "-"))

price = "1.23$"
print(price.replace("$" ,"").replace("." , ""))


# Transformations

first_name = "Turjo"
last_name = "Sarkar"

print(first_name + " " + last_name) # String concatation

folder = "C:/Users/Turjo/"
file = "report.csv"

print(folder + file)

# Formatting

name = "Turjo"
age = 22
is_student = True
print(f"My name is {name}, I am {age} years old. Student status is {is_student}")

print(f"2 + 3 = {2 + 3}")


# Split

stamp = "2026-09-20 14:30"
print(stamp.split(" "))

print("ha" * 3)
