x, y = map(int, input().split())
n = int(input())
garo = [0, x]
sero = [0, y]
for i in range(n):
    po, l = map(int, input().split())
    if po == 1:
        garo.append(l)
    else:
        sero.append(l)
garo.sort(reverse=True)
sero.sort(reverse=True)
for i in range(1, len(garo)):
    garo[i - 1] -= garo[i]
for i in range(1, len(sero)):
    sero[i - 1] -= sero[i]

print(max(garo) * max(sero))
