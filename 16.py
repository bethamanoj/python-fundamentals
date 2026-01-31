n = int(input())
temp = n
sum = 0 
while temp > 0:
	r = temp % 10 
	sum = sum + r
	temp //= 10
print(sum)