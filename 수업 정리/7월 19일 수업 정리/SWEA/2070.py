# import sys

# sys.stdin = open("2070_input.txt", "r")

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    if a > b:
        print(f'#{i + 1} >')
    elif a < b:
        print(f'#{i + 1} <')
    else:
        print(f'#{i + 1} =')