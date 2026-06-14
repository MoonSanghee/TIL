T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    h, w = map(int, input().split())
    maps = [input() for _ in range(h)]
    H, W = 0, 0
    # 영역의 크기를 받고 각 방향으로 칠해야하는 횟수를 담을 변수를 설정해줍니다
    for i in range(h):
        if '.' not in maps[i]:
            H += 1
    for j in range(w):
        for i in range(h):
            if maps[i][j] == '.':
                break
        else:
            W += 1
    # 각 방향으로 칠해야하는 횟수를 확인해줍니다
    if H == h and W == w:
        print(min(h, w))
    else:
        print(H + W)
    # 모든 칸을 칠해야한다면 적게 칠하는 경우를 출력하고 아니라면 둘을 더한 값을 출력해줍니다