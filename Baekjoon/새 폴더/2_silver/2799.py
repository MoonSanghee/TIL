m, n = map(int, input().split())
maps = [input() for _ in range(m * 5 + 1)]
maps = maps[::-1]
result = [0, 0, 0, 0, 0]
# 주어지는 건물의 크기와 건물의 상태를 받고 행을 뒤집어줍니다
# 결과를 담을 변수를 설정해줍니다
for i in range(m):
    for j in range(n):
        r = 1 + i * 5
        c = 1 + j * 5
        for k in range(5):
            if maps[r + k][c] == '*':
                result[4 - k] += 1
                break
        else:
            result[0] += 1
        # 각 방의 시작을 설정하고 행을 뒤집었으므로 방의 행을 순환하며 블라인드 상태를 결과에 담아줍니다

print(*result)
# 주어진 형식에 맞게 출력하여줍니다