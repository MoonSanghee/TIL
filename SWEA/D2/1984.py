import sys

sys.stdin = open("1984_input.txt", "r")

t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    b = sum(a) - max(a) - min(a)
    print(f'#{i + 1} {round(b/8)}')
