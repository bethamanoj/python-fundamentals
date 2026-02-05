ch = input()
s = ""
for i in ch:
	if i not in s:
		s = s + i
print(s)