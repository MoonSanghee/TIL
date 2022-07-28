import sys

sys.stdin = open("2005_input.txt", "r")

t = int(input())
for i in range(1, t + 1):
    print(f'#{i}')
    n = int(input())
    a = [1]
    n += 1
    while n != len(a):
        b = []
        for i in a:
            print(i, end = ' ')
        a = [0] + a + [0]
        for i in range(len(a) - 1):
            b.append(a[i] + a[i + 1])
        a = b
        print()