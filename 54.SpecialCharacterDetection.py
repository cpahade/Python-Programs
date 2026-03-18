def SCD(msg):
    count = 0
    for i in msg:
        if not i.isalnum():
            count += 1
    return count

msg = input("Enter a string: ")
specialcount = SCD(msg)
print(specialcount)