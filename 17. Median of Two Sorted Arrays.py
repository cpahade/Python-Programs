def MedianCalc(num1, num2):
    numbers = num1 + num2
    numbers.sort()
    size = len(numbers)
    if size % 2 == 0:
        mi = size // 2
        return (numbers[mi - 1] + numbers[mi]) / 2.0
    else:
        mi = size // 2
        return numbers[mi]
                         
num1 = [7,18,23]
num2 = [12,6]
median = MedianCalc(num1, num2)
print(median)
