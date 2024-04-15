h, w = map(int, input().split())
maps = [input() for _ in range(h)]
result = [[-1 for _ in range(w)] for _ in range(h)]
# 영역의 크기와 최초 구름의 위치를 받아주고 구름이 도달하는 시간을 표시할 변수를 설정해줍니다.
for i in range(h):
    for j in range(w):
        if maps[i][j] == 'c':
            result[i][j] = 0
            for k in range(j + 1, w):
                if maps[i][k] == 'c':
                    break
                else:
                    result[i][k] = k - j
# 구름을 발견하면 구름이 흘러가는 것을 확인하여 빈 자리에 구름이 도달하는 시간을 표시해줍니다.
for line in result:
    print(*line)
# 각 줄별로 구름이 자리에 도달하는 시간을 출력해줍니다.