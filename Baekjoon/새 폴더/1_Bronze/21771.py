R, C = map(int, input().split())
Rg, Cg, Rp, Cp = map(int, input().split())
room = [input() for _ in range(R)]
# 방의 크기와 배게의 크기, 가희의 크기를 받고 방의 배치를 받아줍니다
cnt = 0
for i in range(R):
    for j in range(C):
        if room[i][j] == 'P':
            cnt += 1
# 배게가 차지하고있는 공간의 크기를 받아줍니다
if cnt == Rp * Cp:
    print(0)
else:
    print(1)
# 배게가 가린 부분이 있는지 확인하여 가희가 배게위에있는지 출력해줍니다