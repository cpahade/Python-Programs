def SecondLargest(arr):
    arr.sort()
    arr = set(arr)
    arr = list(arr)
    print(arr)
    return arr[len(arr)-2]
print(SecondLargest([5,1,2,0,6,3,5,5,6,5]))