#using input

name = input("Enter your name: ") # dynamic 
country = "Bangladesh" # hard coded
print("You are", name)

x = 'A'
print(x)

#Ask for a value
y = input("Enter value:")
print(y)
print(x + y)

# handling multiple inputs 

data = input("Enter your name, age, dept (comma-seperated) :")
name, age, dept = data.split(",")
name = name.strip()
age = int(age.strip())
dept = dept.strip()

print(f"{name} is {age} years old and studying {dept}")