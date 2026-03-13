def Anagramcheck(a,b):
    c = 0
    if len(a) == len(b):
        for i in a:
            if i in b:
                c += 1

    if c == len(a):
        print("Anagram")
    else:
        print("Not an Anagram")

Anagramcheck("listen","silent")