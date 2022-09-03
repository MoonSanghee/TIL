n, m = map(int, input().split())
maps = []
for i in range(n):
    num = str(input())
    line = list(map(int, num))
    maps.append(line)

length = min(n, m)
a = 0
while a == 0 and length>1:
    for i in range(n - length + 1):
        for j in range(m - length + 1):
            check = [maps[i][j], maps[i][j + length - 1], maps[i + length - 1][j], maps[i + length - 1][j + length - 1]]
            if len(set(check)) == 1:
                a = 1
                break
    if a == 0:
        length -= 1
        
print(length**2)