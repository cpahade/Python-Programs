def CommonNumber(A,B,C):
    count = 0
    for i in A:
        if i in B and i in C:
            print(i)

A = [1,5,12,9]
B = [7,5,9,12]
C = [8,7,12,9]
CommonNumber(A,B,C)