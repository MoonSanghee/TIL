n = int(input())
maps = [0]
for i in range(n):
    maps.append(int(input()))

best = 0
def check(x, y):
    global best
    ate = maps[x]
    if y > best:
        best = y
    for i in range(x, n + 1):
        if maps[i] > ate:
            ate = maps[i]
            check(i, y + ate)
            ate = maps[x]
for i in range(n + 1):
    check(i, 0)
print(best)