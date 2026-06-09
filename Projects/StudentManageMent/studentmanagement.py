
students = []
id = 0

while True: 
    print("1. Add Student \n2. View Students \n3. Search Student \n4. Exit \n")
    choice = int(input("Enter your choice : "))
    match choice:
        case 1 :
            id = id + 1
            students.append({
                "id" : id,
                "name" : input("\nEnter student's name : "),
                "dept" : input("\nEnter dept: ")
                })
            print("Student added successfully!")
        case 2:
            for i in students:
                print(i)
            if not students:
                print("Not found!")
        case 3:
            search_for = int(input("Enter the student's id you are searching for : "))
            found = False
            for i in students:
                if i["id"] == search_for :
                    print("Found!")
                    print(i)
                    found = True
            if not found: print("NOT FOUND!!!!!!")
        case 4:
            surity = input("Are you sure? (yes/no)")
            if surity == "yes"  :  break



