n = int(input())
# 좌표의 개수를 받아줍니다.
rent = set()
# 빌린 영역을 담을 셋 구조를 만들어줍니다.
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            rent.add((i, j))
            # 좌표를 받고 좌표 안의 지점을 순회하며 x,y좌표를 묶어 rent에 넣어줍니다.

print(len(rent))
# rent의 길이를 출력해줍니다.