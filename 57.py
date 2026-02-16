n = int(input())
temp = n
m = n
count = 0
k = 0
while temp > 0:
    r = n%10
    count += 1
    temp //= 10
while m >0:
    r = m % 10 
    k = k + (r**count)
    m //= 10
if (n == k):
    print('Armstrong ')
else:
    print('Not a armstrong')
	