W, N = input().split()
N = int(N)
# 뒤집는 방향과 배열의 크기를 받아줍니다
maps = [list(map(int, input().split())) for _ in range(N)]
new = [["?"] * N for _ in range(N)]
# 주어진 크기의 배열을 받고 같은 크기의 뒤집은 결과를 담을 변수를 설정해줍니다
d = {1 : 1, 2 : 5, 5 : 2, 8 : 8}
# 뒤집을 수 있는 숫자들의 뒤집기 전후를 키, 밸류로 묶어 딕셔너리에 담아줍니다 
if W in "UD":
    for i in range(N):
        for j in range(N):
            if maps[i][j] in d:
                new[N - i - 1][j] = d[maps[i][j]]
else:
    for i in range(N):
        for j in range(N):
            if maps[i][j] in d:
                new[i][N - 1 - j] = d[maps[i][j]]
# 뒤집는 방향에 따라 배열을 순회하며 뒤집었을때 담길 위치에 값을 뒤집은 결과로 수정해줍니다
for line in new:
    print(*line)
# 결과를 차례대로 출력해줍니다