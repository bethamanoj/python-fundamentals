n = int(input())
temp = n
count = 0
while temp > 0:
	count += 1
	temp//= 10
print(count)