n = int(input())
s = input().split()
d = []

for i in range(n):
    s[i] = int(s[i])

for i in range(n):
    d.append(s[i])

for i in range(n-1, -1, -1):
    print(d[i], end=' ')