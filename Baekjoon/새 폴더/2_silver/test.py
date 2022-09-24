n, m = map(int, input().split())
maps = [[0] * (n + 1)]
for i in range(n):
    line = [0] + list(map(int, input().split()))
    maps.append(line)
