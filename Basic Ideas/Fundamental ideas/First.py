spam_amount = 0
print(spam_amount)

spam_amount += 4

if(spam_amount > 0) :
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)


#assigning zero -> comment line
spam_amount = 0
print(spam_amount)

a = 5
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b) # True division -> also gives float
print(a // b) # Integer division -> always rounded down to next int
print(a % b)
print(a ** b)
print(-a)


# Order of operations -> follows PEMDAS

# Parenthesis -> Exponents -> Multiplication/Division -> Addition/Subtraction


hat_height_cm = 25
my_height_cm = 190

# How tall am I, in meters, when wearing my hat?

total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters = ", total_height_meters, "?")

# This is not ok, here, parenthesis is important

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters : ", total_height_meters)

# min and max function

print(min(1, 2, 3))
print(max(1, 2, 3))
print(abs(-10)) 

print(float(10))
print(int(5.5))

print(int('807') + 1)
