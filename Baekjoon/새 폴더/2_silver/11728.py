n, m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(m):
    a.append(b[i])
a.sort()
print(*a)