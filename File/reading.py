# reading entire files 

with open ("data.txt", "r") as file:
    content = file.read()
    print(content)

# read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())


# read all lines into list
with open("data.txt", "r") as file:
    lines = file.readline()