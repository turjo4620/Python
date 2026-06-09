# Tuples are immutable -> cannot be changed

coordinates = (10, 20)
point = (x, y) = (2, 3)

# accessing 
print(coordinates[0])

x, y = coordinates # unpacking
print(x, y)

# when immutable data needed
colors = ("red", "green", "blue")

