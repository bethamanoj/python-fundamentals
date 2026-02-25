n = list(map(int,input().split()))
k = len(n)+1
expected = k*(k+1) // 2
actual = sum(n)
l = expected - actual
print(l)