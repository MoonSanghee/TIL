n, m = map(int, input().split())
k = int(input())
sheet = [input() for _ in range(n)]
JOI = [[[0,0,0] for _ in range(m + 1)] for _ in range(n + 1)]
# 영역의 크기와 확인할 범위를 받고 영역을 받은 후 영역의 누적합을 담을 리스트를 만들어줍니다.

for i in range(n):
    for j in  range(m):
        JOI[i + 1][j + 1][0] = JOI[i + 1][j][0] + JOI[i][j + 1][0] - JOI[i][j][0]
        JOI[i + 1][j + 1][1] = JOI[i + 1][j][1] + JOI[i][j + 1][1] - JOI[i][j][1]
        JOI[i + 1][j + 1][2] = JOI[i + 1][j][2] + JOI[i][j + 1][2] - JOI[i][j][2]
        if sheet[i][j] == 'J':
            JOI[i + 1][j + 1][0] += 1
        elif sheet[i][j] == 'O':
            JOI[i + 1][j + 1][1] += 1
        else:
            JOI[i + 1][j + 1][2] += 1
# 각 자리를 확인하여 영역의 누적합을 표시해줍니다.

for _ in range(k):
    a, b, c, d = map(int, input().split())
    j = JOI[c][d][0] - JOI[c][b - 1][0] - JOI[a - 1][d][0] + JOI[a - 1][b - 1][0]
    o = JOI[c][d][1] - JOI[c][b - 1][1] - JOI[a - 1][d][1] + JOI[a - 1][b - 1][1]
    i = JOI[c][d][2] - JOI[c][b - 1][2] - JOI[a - 1][d][2] + JOI[a - 1][b - 1][2]
    print(j, o, i)
    # 영역의 누적합을 이용하여 각 영역의 개수를 확인하여 출력해줍니다.