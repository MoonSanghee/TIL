even = int(input())
if even == 1:
    odd = 2
else:
    odd = 1
# 홀수와 짝수 번째 플레이어의 번호를 받아줍니다.
bingo = [[0]*3 for _ in range(3)]
# 틱택토 게임판을 만들어줍니다.
for i in range(9):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    flag = False
    # 입력칸의 좌표를 받고 게임이 종료되는지 확인할 변수를 설정해줍니다.

    if i % 2 == 0:
        bingo[x][y] = even
    else:
        bingo[x][y] = odd
    # 플레이어의 입력을 표시해줍니다.

    for j in range(3):
        if bingo[x][j] != bingo[x][y]:
            break
    else:
        flag = True
    
    for j in range(3):
        if bingo[j][y] != bingo[x][y]:
            break
    else:
        flag =True
    
    if bingo[0][0] == bingo[1][1] == bingo[2][2] and bingo[1][1] != 0:
        flag = True
    
    if bingo[2][0] == bingo[1][1] == bingo[0][2] and bingo[1][1] != 0:
        flag = True
    # 게임이 완료되는지 확인해줍니다.
    if flag:
        print(bingo[x][y])
        break
    # 완료 되었다면 이긴 유저의 번호를 출력해줍니다.
else:
    print(0)
    # 완료되지 않았다면 무승부를 출력해줍니다.