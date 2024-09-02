t = int(input())

for tc in range(t):
    a, b = map(int, input().split())
    if b % a == 0 and b // a >= 2:
        print(1)
    else:
        print(0)