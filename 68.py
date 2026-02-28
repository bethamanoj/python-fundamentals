n = int(input())
k = 2
for i in range(1,n+1):
    if n == i:
        print(k)
    else:
        print(k,end=",")
        k = 2 * (3 ** i)