# creating dictionaries 

student = { 
    "name" : "Turjo",
    "age" : 21,
    "dept" : "CSE",
    "grades" : [80, 85, 82, 90, 95]
}

# accessing values

print(student["name"])
print(student["age"])
print(student["dept"])
print(student["grades"])

# modifying dictionaries 

student["age"] = 25
student["dept"] = "Computer Science"

del student["grades"]

print(student)

# iterating 

for key, value in student.items():
    print(f"{key} : {value}")

# Dictionary comprehension

squares_dict = {x : x ** 2 for x in range(5)}
print(squares_dict)