# 백준 11047
n, v = map(int, input().split())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

cnt = 0
for i in range(n - 1, - 1, -1):
    cnt += (v // numbers[i])
    v %= numbers[i]
print(cnt)