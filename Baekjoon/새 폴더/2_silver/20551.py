import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()
d = dict()

for i in range(n):
    if numbers[i] not in d:
        d[numbers[i]] = i

for _ in range(m):
    num = int(input())
    if num in d:
        print(d[num])
    else:
        print(-1)