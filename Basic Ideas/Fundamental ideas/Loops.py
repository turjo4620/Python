# for loop

for i in (1,2,3,4,5):
    print(f"Round : {i}")

items = (1,2,3,4,5)

for item in items:
    print(item)

# range

for i in range(5):
    print(i) # starts from zero and stops just before 5

for i in range(1, 5):
    print(i) # not include the 5

for i in range (2, 10, 2):
    print(i) # last one is steps


# Finding summation

scores = [10, 20, 15, 12, 13]
total = 0

for score in scores:
    total += score
    print("Current total: ", total)
print("Final total: ", total)

files = [' Report.csv', 'Data.csv', 'final.txT  ']

for file in files:
    file = file.strip().lower()
    print(f"Processing {file}")


# Break and continue

#continue skips and break stops


#while loops

i = 0
while i < 10:
    print(i)
    i += 1

while True:
    prompt = input("Enter your name: ")
    print(prompt)
    if(prompt == "stop"):
        break


for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)