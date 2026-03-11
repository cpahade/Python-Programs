def main():
    binary = input("Enter a Binary Number: ")
    decimal = 0
    power = len(binary) - 1
    for d in binary:
        if (d == '0' or d == '1'):
            decimal += int(d)*(2**power)
            power -= 1
        else:
            print("Invalid Input")
            exit()
    print(f"Decimal Equivalent: {decimal}")

main()
