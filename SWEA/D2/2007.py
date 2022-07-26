import sys

sys.stdin = open("2007_input.txt", "r")

T = int(input())
for i in range(T):
    a = input()
    b = []
    for j in range(1, 11):
        lst = [a[i:i + 11 - j] for i in range(0, 30, 11 - j)]
        if lst[0] == lst[1]:
            b.append(11 - j)
    print(f'#{i + 1} {min(b)}')