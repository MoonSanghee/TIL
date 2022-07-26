t = int(input())
for i in range(t):
    n = int(input())
    a = []
    for j in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    print(a)