def add():
    n1 = int(input("Enter value of n1: "))
    n2 = int(input("Enter value of n2: "))
    print("The sum of n1 and n2 is: ", n1 + n2)

def calc():
    n1 = int(input("Enter value of n1: "))
    n2 = int(input("Enter value of n2: "))
    sum = n1 + n2
    mul = n1 * n2
    sub = n1 - n2
    div = n1 / n2
    return sum, sub, mul, div

"""
Four types of arguments we can pass in fuction:
1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable Length Arguments
"""

def personalInfo(fname, lname):
    print("First Name:", fname)
    print("Last Name:", lname)

def cityName(city = "Nagpur"):
    print(city)

def studentName(*name):
    print(name)






def main():
    # add()
    # result = calc()
    # print(result)
    # fname = "Chaitanya"
    # lname = "Pahade"
    # personalInfo(lname, fname)
    # cityName("Mumbai")
    # cityName("Delhi")
    # cityName()
    studentName("Luffy", "Eren", "Ichigo", "Light", "Asta")








if __name__ == "__main__":
    main()