n = int(input())
sheet = [list(map(int, input().split())) for _ in range(n)]
# 영역의 크기와 2중 리스트를 받아줍니다.
papers = [0, 0, 0]
# -1, 0, 1 종이의 개수를 담아줄 리스트를 만들어줍니다.
def check(x, y, size):
    # x, y좌표와 확인할 영역의 크기를 받앙줍니다.
    base = sheet[x][y]
    # x, y좌표를 기준으로 기준을 정해줍니다.
    for i in range(size):
        for j in range(size):
            if sheet[x + i][y + j] != base:
                # 확인하는 영역안에 기준이 아닌 종이가 있다면
                for i2 in range(3):
                    for j2 in range(3):
                        check(x + i2 * size // 3, y + j2 * size // 3, size // 3)
                return
                # 3분할하여 함수를 재귀하여 실행시키고 기존의 함수는 작동을 멈추어줍니다.
    if base == -1:
        papers[0] += 1
    elif base == 0:
        papers[1] += 1
    else:
        papers[2] += 1
    # 확인 결과 종이가 모두 같은 종류라면 어떤 종이인지 확인하여 리스트에 담아줍니다.

check(0, 0, n)
# 확인 함수를 실행시켜줍니다.
for i in papers:
    print(i)
    # 리스트에 담긴 종이의 개수를 차례대로 출력해줍니다.