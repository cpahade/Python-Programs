maths = int(input("Enter your Maths mark: "))
english = int(input("Enter your English mark: "))
chemi = int(input("Enter your Chemistry mark: "))

total = maths + english + chemi
percentage = (total/300)*100

if percentage >= 60:
    print("You're eligible for placement")
else:
    print("You're eligible for placement")