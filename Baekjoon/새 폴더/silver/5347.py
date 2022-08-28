t = int(input())
for i in range(t):
    a, b =map(int, input().split())
    c = min(a, b)
    for i in range(1, c):
        if a % i == 0 and b % i == 0:
            a //= i
    print(a * b)