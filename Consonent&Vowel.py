string  = input("Enter a String")
vowels = ["a", "e", "i", "o", "u"]
vcount = 0

string.lower()
for char in string:
    if char in vowels:
        vcount += 1
conscount = len(string) - vcount
print(f"Number of vowels: {vcount}")
print(f"Number of consonants: {conscount}")