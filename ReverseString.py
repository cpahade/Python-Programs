string = (input("Enter a String: ")).lower()
reverse_string = ""
for i in range(len(string)-1,-1,-1):
    reverse_string += string[i]

print(reverse_string)