t = int(input())
for i in range(t):
    H, W, N = map(int, input().split())
    # H는 높이, W는 길이, N은 손님의 방문 순서이다.
    if (N % H) == 0:
        print(H * 100 + (N // H))
    else:
        print((N % H) * 100 + (N // H) + 1)