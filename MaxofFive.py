a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
d = int(input("Enter another number: "))
e = int(input("Enter another number: "))

if a > b and a > c and a > d and a>e:
    print(f"{a}is maximum")
if b > a and b > c and b > d and b > e:
    print(f"{b}is maximum")
if c > a and c > b and c > d and c > e:
    print(f"{c}is maximum")
if d > a and d > b and d > c and d > e:
    print(f"{d}is maximum")
if e > a and e > b and e > d and e > e:
    print(f"{e}is maximum")