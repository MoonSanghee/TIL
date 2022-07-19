import sys

sys.stdin = open("2056_input.txt", "r")

T = int(input())
for i in range(T):
    a = int(input())
    D = a % 100
    M = a % 10000 // 100
    Y = a // 10000
    if M in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= D <= 31:
            c = '%04d/%02d/%02d' %(Y, M, D)
            print(f'#{i + 1} {c}')
        else:
            print(f'#{i + 1} -1')
    elif M in [4, 6, 9, 11]:
        if 1 <= D <= 30:
            c = '%04d/%02d/%02d' %(Y, M, D)
            print(f'#{i + 1 } {c}')
        else:
            print(f'#{i + 1 } -1')
    elif M == 2:
        if 1 <= D <= 28:
            c = '%04d/%02d/%02d' %(Y, M, D)
            print(f'#{i + 1 } {c}')
        else:
            print(f'#{i + 1} -1')
    else:
        print(f'#{i + 1} -1')

