a = int(input())
b = int(input())
c = int(input())
if (a>b and a<c) or (a>c and a<b):
	print(a,' is second largest')
elif (b>c and b<a) or (b>a and b<c):
	print(b,' is second largest')
else:
	print(c,' is second largest')