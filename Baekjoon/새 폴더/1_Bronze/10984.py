t = int(input())
for _ in range(t):
    n = int(input())
    total = 0
    result = 0
    for i in range(n):
        cnt, point = list(map(float, input().split()))
        total += cnt
        result += cnt * point
    print(int(total),round(result / total, 1))