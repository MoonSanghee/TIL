papper = [[0]*100 for _ in range(100)]
# 100 * 100 크기의 도화지를 설정해줍니다.
n = int(input())
# 종이를 몇 장 깔것인지 받아줍니다.

for _ in range(n):
    x, y = map(int, input().split())
    # 두 종이의 가로 세로 시작 위치를 받아줍니다.
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            papper[i][j] = 1
            # 색종이는 10 * 10의 크기이므로 시작점으로부터 가로, 세로로 10 만큼의
            # 영역에 종이가 놓여있다는 표시를 해줍니다.
            # 색종이가 몇장이 겹치든 놓여있다는 표시만 해주기때문에 값을 따로
            # 확인하지 않고 1로 저장해줍니다.

cnt = 0
for i in range(100):
    for j in range(100):
        if papper[i][j]:
            cnt += 1
            # 흰 종이의 모든 영역을 순회하며 색종이가 놓여진 영역이 몇 칸인지 확인해줍니다.

print(cnt)
# cnt에 저장된 값을 출력해줍니다.