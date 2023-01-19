n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(str, input())))

result = 0

for i in range(n):
    cnt = 0
    vertical = 1
    for j in range(m):
        if maps[i][j] == '|':
            vertical = 1
        else:
            if vertical == 1:
                cnt += 1
            vertical = 0
    # 세로줄이 들어왔었다고 설정을 해두고 가로줄이 들어오면 가로줄이 들왔다는 표시를 해주고
    # 판자가 1개 더 필요하다고 세어줍니다.
    result += cnt
    # 행 순환이 끝나면 최종 결과에 필요한 판자를 더해줍니다.
for i in range(m):
    cnt = 0
    vertical = 0
    for j in range(n):
        if maps[j][i] != '|':
            vertical = 0
        else:
            if vertical == 0:
                vertical = 1
                cnt += 1
    result += cnt
    # 열을 순회하며 필요한 판자를 더하여 최종 결과에 더해줍니다.
print(result)
# 출력을 해줍니다.