import sys

sys.stdin = open("1948_input.txt", "r")

t = int(input())
for i in range(1, t + 1):
    a, b, c, d = map(int, input().split())
    M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if a == c:
        print(f'#{i} {d - b + 1}')
    else :
        print(f'#{i} {sum(M[a - 1:c - 1]) + d - b + 1}')

# M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(M[2:6])
