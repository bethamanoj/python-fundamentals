n = int(input())
fact = 1
temp = n
k = 0
while temp > 0:
    r = temp %10
    for i in range(1,r+1):
        fact = fact * i
    k = k + fact 
    fact = 1
    temp //= 10
if (k == n):
    print('Strong Number')
else:
    print('Not')