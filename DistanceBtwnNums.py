def TotalDistance(l, numarray):
    i = 0
    sum = 0
    for i in range(l-1):
        distance = abs(numarray[i+1] - numarray[i])
        sum += distance
    print(sum)

array = [10,11,7,12,14]
TotalDistance(len(array),array)
