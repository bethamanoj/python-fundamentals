n = list(map(int,input().split()))
seen = set()
duplicate = set()
for i in n:
	if i in seen:
		duplicate.add(i)
	else:
		seen.add(i)
print(list(duplicate))