coins = [500, 100, 50, 10, 5, 1]
cnt = 0
n = 1000 - int(input())
for i in range(6):
    cnt += n // coins[i]
    n %= coins[i]
print(cnt)