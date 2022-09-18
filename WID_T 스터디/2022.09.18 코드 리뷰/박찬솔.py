# 백준 13458
room = int(input())
takers = list(map(int, input().split()))
main, sub = map(int, input().split())
cnt = 0
for i in takers:
    if i - main <= 0:
        cnt = 1
    else:
        i -= main
        cnt += 1
        cnt += i // sub
        if i % sub != 0:
            cnt += 1

print(cnt)