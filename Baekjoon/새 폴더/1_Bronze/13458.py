room = int(input())
takers = list(map(int, input().split()))
main, sub = map(int, input().split())
cnt = room
for i in takers:
    i -= main
    if i > 0:
        if i % sub:
            cnt += (i // sub) + 1
        else:
            cnt += i // sub

print(cnt)