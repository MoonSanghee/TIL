import sys

sys.stdin = open("1966_input.txt", "r")

t = int(input())
for i in range(t):
    n = int(input())
    nl = map(int, input().split())
    a = sorted(list(nl))
    print(f'#{i + 1}', end = ' ')
    for j in range(n):
        print(a[j], end = ' ')
    print()