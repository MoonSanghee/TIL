def solution(m, n, puddles):
    answer = 0
    maps = [[0] * (n + 1) for _ in range(m + 1)]
    p = [[x, y] for [x, y] in puddles]
    # 웅덩이의 좌표를 받아줍니다.
    maps[1][1] = 1
    # 시작점에 도달하는 방법 1개로 표시해 줍니다.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                continue
            # 시작 좌표가 아니라면
            if [i, j] in p:
                maps[i][j] = 0
            # 웅덩이가 있는 위치일 경우 지나갈 수 없고
            else:
                maps[i][j] = (maps[i - 1][j] + maps[i][j - 1])%1000000007
            # 아니라면 오른쪽이나 아래로만 움직이므로 왼쪽의 좌표와 위의 좌표값의
            # 합을 1000000007을 나눈 나머지를 넣어줍니다.
    return maps[-1][-1]
    # 마지막에 도착한 칸에 저장된 수를 출력해줍니다.
