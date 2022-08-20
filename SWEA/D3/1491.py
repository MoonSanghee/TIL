import sys
sys.stdin = open('1491_input.txt', 'r')

test = int(input())
for t in range(1, test + 1):
    n, a, b = map(int, input().split())
    mini = n * a * b
    for r in range(1, n + 1):
        c = 1
        while r * c <= n:
            result = a * abs(r - c) + b * (n - r * c)
            mini = min(mini, result)
            c += 1
    print(f'#{t} {mini}')