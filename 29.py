n = int(input())	
k = 0				   
for i in range(1,n):		   
	if (n % i == 0):	 
		k = k + i	   
if (k == n):			   
	print('Perfect Number')
else:
	print('Not a Perfect Number')