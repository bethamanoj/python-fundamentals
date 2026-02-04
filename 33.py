ch = input()
c = 0 
count = 0
for i in ch:
	if i in 'aeiouAEIOU':
		count += 1
	elif i in ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z':
		c += 1
print('Number of vowels are ',count)
print('Number of cosonants are ',c)