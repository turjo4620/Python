#write to file

with open("output.txt", "w") as file:
    file.write("Hello\n")
    file.write("Hi\n")

#append to file

with open("output.txt", "a") as file:
    file.write("append done")