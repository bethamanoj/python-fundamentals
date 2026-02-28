n = int(input())
k = 2
for i in range(1,n+1):
    if n == i:
        print(k,end=',...')
    else:
        print(k,end=",")
        k = k + (i+1)+1