t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    print(f'#{i + 1} {round(sum(a)/10)}')