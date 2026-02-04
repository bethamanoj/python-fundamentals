ch = input()
s = ""
for i in ch:
	if i not in s:
		c = 0
		for j in ch:
			if i == j:
				c += 1
		print(i,'=',c)
		s = s+i