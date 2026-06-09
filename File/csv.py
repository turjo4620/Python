import csv

# reading csv

# with open ("data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

#writing csv
with open ("output.csv", "w", newline= "") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Dept"])
    writer.writerow(["Turjo", 21, "CSE"])