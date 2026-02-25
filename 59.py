n = input()
k = input()
m = n.lower()
l = k.lower()
if sorted(m)==sorted(l):
	print('Anagram')
else:
	print('Not a Anagram')