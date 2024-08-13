n = int(input())
paper = set()
# 놓읋 검은 색종이의 개수를 받고 검은 색종이가 놓여진 좌표를 표시할 세트형 구조를 만들어줍니다.
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper.add((x + i, y + j))
# 색종이를 놓는 위치를 받고 검은 색종이가 위치하는 좌표를 세트에 넣어줍니다.
result = 0
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
# 둘레를 담을 변수와 둘레인지 확인하기위해 4방위 탐색을 설정해줍니다.
for x, y in paper:
    outside = 0
    # 외부와 접촉하고 있는 면의 수를 담을 변수를 만들어줍니다
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if (nx, ny) not in paper:
            outside += 1
        # 4방위 탐색을 통해 외부와 접하고 있는 면의 수를 확인해줍니다
    if outside == 2:
        result += 2
    elif outside == 1:
        result += 1
    # 외부와 한 면만 닿아있다면 1, 2면이 닿아있다면 2를 더해줍니다.

print(result)
# 결과를 출력해줍니다.