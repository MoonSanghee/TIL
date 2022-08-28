n = int(input())
maps = [[]] + [[]] * n
check = [0] * (n + 1)
for i in range(n - 1):
    a, b = map(int, input().split())
    maps[a].append(b)
    
