for i in range(1,5):
    if i == 3:
        break
    print(i)

print()

for i in range(1,5):
    if i == 3:
        continue
    print(i)

print()

for x,y in zip((range(1,6)),(range(5,0,-1))):
    if x == 3 and y == 3:
        continue
    print(x,y)

print()

i = 1
while i <= 5:
    print(i)
    i += 1

print()

username = ""
password = ""
while username!="admin" and password!="pass":
    username = input("Enter your username: ")
    password = input("Enter your password: ")



string = input("Enter a String: ")
string = string.lower()
reverse_string = ""
for i in range(len(string)-1,-1,-1):
    reverse_string += string[i]
if reverse_string == string: print("Palindrome")
else: print("Not Palindrome")

for i in range(1,4):
    for j in range(1,4):
        print(i, end=" ")
    print()