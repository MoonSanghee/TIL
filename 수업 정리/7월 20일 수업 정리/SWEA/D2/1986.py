import sys

sys.stdin = open("1986_input.txt", "r")

t = int(input())

for i in range(t):
    a = int(input())
    result = 0
    for j in range(1, a + 1):
        if j % 2 == 0:
            result -= j
        else:
            result += j
    print(f'#{i + 1} {result}')


