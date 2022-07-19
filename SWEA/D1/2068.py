# import sys

# sys.stdin = open("2068_input.txt", "r")

t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    print(f'#{i + 1} {max(a)}')