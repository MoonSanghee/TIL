test = int(input())
for t in range(1, test + 1):
    n, k = map(int, input().split())
    points = list(map(int, input().split()))
    points.sort(reverse = True)
    result = 0
    for i in range(k):
        result += points[i]
    print(f'#{t} {result}')