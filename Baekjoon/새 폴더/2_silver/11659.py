import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
for i in range(1, n):
    numbers[i] += numbers[i - 1]
for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        print(numbers[j - 1])
    else:
        print(numbers[j - 1] - numbers[i - 2])