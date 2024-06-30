x, y, p1, p2 = map(int, input().split())
# 두 사람의 시작점과 한 번에 이동하는 거리를 받아줍니다.
while True:
    if p1 == p2:
        print(p1)
        break
    # 두 사람이 만나면 그 지점을 출력하고 멈추어줍니다.
    elif p1 > 1e5:
        print(-1)
        break
    # a의 위치가 충분히 멀어졌는데 만나지 못한다면 두 사람이 만나지 못한다고 출력해줍니다.
    elif p1 < p2:
        p1 += x
    else:
        p2 += y
        # 두 사람의 위치를 확인하여 뒤의 사람을 이동해줍니다.