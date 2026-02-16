n = int(input())
k = 0
for i in range(1,n):
    if n % i == 0 :
        k = k+i
if (n == k):
    print('Perfect Number')
else:
    print('Not ')