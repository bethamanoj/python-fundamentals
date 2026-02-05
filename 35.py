c = input()
n = int(input())
k = input()
s = ''
for i in range(len(c)):
    if (i+1)%n==0:
        s = s+k
    else:
        s = s+c[i]
print(s)