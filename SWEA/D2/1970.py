import sys

sys.stdin = open("1970_input.txt", "r")


t = int(input())
for i in range(t):
    a = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    b = int(input())
    print(f'#{i + 1}')
    for j in range(8):
        print(b // a[j], end = ' ')
        if b // a[j] != 0:
            b %= a[j]
    print()