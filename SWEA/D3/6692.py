t = int(input())
for test in range(1, t + 1):
    n = int(input())
    result = 0
    for i in range(n):
        p1, p2 = map(float, input().split())
        result += p1 * p2
    print(f'#{test} {result}')