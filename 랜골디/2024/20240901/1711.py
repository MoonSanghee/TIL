import sys
input = sys.stdin.readline

n = int(input())
# 주어지는 좌표의 개수를 받아줍니다.
dot = []

for _ in range(n):
    point = tuple(map(int, input().split()))
    dot.append(point)
# n개의 좌표를 튜플로 받아 리스트에 담아줍니다.
cnt = 0
# 직각 삼각형의 개수를 담을 변수를 설정합니다.
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            x1, y1 = dot[i][0], dot[i][1]
            x2, y2 = dot[j][0], dot[j][1]
            x3, y3 = dot[k][0], dot[k][1]
            a = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
            b = ((x2 - x3) ** 2) + ((y2 - y3) ** 2)
            c = ((x3 - x1) ** 2) + ((y3 - y1) ** 2)
            if max(a, b, c) * 2 == a + b + c:
                cnt += 1
            # 세 점을 뽑아 직각 삼각형이 되면 cnt를 갱신해줍니다.

print(cnt)
# cnt에 담긴 값을 출력해줍니다.