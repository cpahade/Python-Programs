maths = int(input("Enter Maths Marks: "))
phy = int(input("Enter Physics Marks: "))
english = int(input("Enter English Marks: "))

if maths > phy:
    if maths > english:
        print("Maths marks are greatest")
    else:
        print("English marks are greatest")
else:
    if phy > english:
        print("Physics marks are greatest")
    else:
        print("English marks are greatest")
