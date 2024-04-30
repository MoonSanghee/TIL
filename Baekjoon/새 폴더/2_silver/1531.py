n, m = map(int, input().split())
maps = [[0 for _ in range(100)] for _ in range(100)]
# 가릴 종이의 개수와 가려지려면 몇 개의 종이가 덮혀야하는지 받고 종이가 덮혀진것을 표시할 영역을 만들어줍니다.
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            maps[i - 1][j - 1] += 1
# n장의 종이를 입력받아 덮어진 영역을 표시해줍니다.
cnt = 0
for i in range(100):
    for j in range(100):
        if maps[i][j] > m:
            cnt += 1
# 영역에서 충분히 덮힌 부분이 몇개인지 확인해줍니다.
print(cnt)
# 결과를 출력해줍니다.