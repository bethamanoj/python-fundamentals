n = int(input())
k = 5
m = 4
for i in range(1,n+1):
    if n == i:
        print(k,end=',...')
    else:
        print(k,end=",")
        k = k + m
        m = m+1