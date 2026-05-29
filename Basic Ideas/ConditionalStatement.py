score = 100
if score >= 90:
    print("A") # indentation is too much important
    print("Good")
elif score >= 80:
    print("B")
    print("Not bad")
else:
    print("F")
    print("Bad")


# Inline if/else

print("A" if score >= 90 else "F")
print("A" if score >= 90 else "B" if score >= 80 else "F")


country = "Bangladesh"

match country:
    case "Bangladesh":
        print("BD")
    case _:
        print("Unknown")