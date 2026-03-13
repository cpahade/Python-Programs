word = input("Enter a word: ")
new_word = ""
for i in word:
    if i not in new_word:
        new_word += i
print(new_word)