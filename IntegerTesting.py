def main():
    number = int(input("Enter a number: "))
    if number > 0:
        print(number,"is positive")
    elif number < 0:
        print(number,"is negative")
    else:
        print("zero")


for i in range(1,4):
    main()