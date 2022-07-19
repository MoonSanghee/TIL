# import sys

# sys.stdin = open("2072_input.txt", "r")

t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    b = 0
    for j in a:
        if (j % 2) == 1:
            b += j
    print(f'#{i + 1} {b}')