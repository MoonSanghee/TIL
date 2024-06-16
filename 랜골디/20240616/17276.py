t = int(input())
# 테스트 케이스의 수를 받아줍니다.
for tc in range(t):
    n, d = map(int, input().split())
    # 영역의 크기와 움직이는 각도를 받아줍니다.
    maps = [list(map(int, input().split())) for _ in range(n)]
    base = [n // 2, n // 2]
    # 주어지는 배열을 받고 가운데 좌표를 받아줍니다.
    if d < 0:
        d += 360
    d //= 45
    d = 8 - d
    # 움직이는 각도가 음수라면 360을 더해 양수로 바꾸어주고 45의 배수가 주어지므로 8분할 변화가 일어납니다
    for i in range(1, n // 2 + 1):
        line = []
        dots = []
        # 기존 좌표의 값과 바뀔 좌표를 받아줍니다
        for x, y  in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                new = (base[0] + x * i, base[1] + y * i)
                dots.append(new)
                line.append(maps[new[0]][new[1]])
        line = line[d:] + line[:d]
        # 위에서 구한 이동하는 각도만큼 값을 갱신해줍니다.
        for j in range(8):
             maps[dots[j][0]][dots[j][1]] = line[j]
            #  좌표를 순회하며 갱신한 값을 배열에 넣어줍니다.
    
    for line in maps:
        print(*line)
        # 배열을 줄별로 출력해줍니다.