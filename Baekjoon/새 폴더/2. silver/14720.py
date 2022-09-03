cnt = 0

length = int(input())
menu = list(map(int, input().split()))

order = [0, 1, 2]
for i in range(length):
    if menu[i] == order[cnt % 3]:
        cnt += 1

print(cnt)