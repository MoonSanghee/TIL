# 백준 1244
def change(a):
    if maps[a] == 1:
        maps[a] = 0
    elif maps[a] == 0:
        maps[a] = 1
n = int(input())
maps = [-1] + list(map(int,input().split()))
t = int(input())
for i in range(t):
    x, p = map(int, input().split())
    if x == 1:
        for j in range(p, n + 1, p):
            change(j)
    else:
        change(p)
        for j in range(1, n):
            if p + j in range(n + 1) and p - j in range(n + 1) and maps[p + j] == maps[p - j]:
                change(p + j)
                change(p - j)
            else:
                break
for i in range(1, n + 1):
    print(maps[i], end = ' ')
    if i % 20 == 0:
        print()