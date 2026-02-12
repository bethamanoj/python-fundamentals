def fact(n):
	k = 1
	for i in range(1,n+1):
		k =  k*i
	return k
n = int(input())
print(fact(n))