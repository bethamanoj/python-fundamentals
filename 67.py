n = int(input())
k = 8
m = 5
for i in range(1,n+1):
    if n == i:
        print(k,end = ",...")
    else:
        print(k,end=",")
        k = k + m
        m = m+1