from collections import deque
maps = [list(map(int, input().split())) for _ in range(5)]
# 주어지는 빙고판을 받아줍니다.
visited = [[False for _ in range(5)] for _ in range(5)]
# 빙고판에서 나온 숫자를 확인할 리스트를 만들어줍니다.
call = []
for i in range(5):
    call += list(map(int, input().split()))
# 부르는 숫자를 차례대로 담아줍니다.

def check():
    # 빙고가 완성된것을 확인하는 함수입니다.
    bingo = 0
    # 완성된 빙고의 줄수를 담을 변수입니다.
    for i in range(5):
        for j in range(5):
            if visited[i][j] == False:
                break
        else:
            bingo += 1
    # 가로줄이 완성된것을 확인하는 단계입니다.
    for i in range(5):
        for j in range(5):
            if visited[j][i] == False:
                break
        else:
            bingo += 1
    # 세로줄이 완성된것을 확인하는 단계입니다.
    for i in range(5):
        if visited[i][i] == False:
            break
    else:
        bingo += 1

    for i in range(5):
        if visited[i][4 - i] == False:
            break
    else:
        bingo += 1
    # 두 대각선이 완성된것을 확인하는 단계입니다.
    return bingo
    # 완성된 빙고가 몇줄인지 리턴합니다.

cnt = 0
# 몇 번째 수를 부르는지 담을 변수입니다.
while True:
    if check() >= 3:
        break
    # 완성된 빙고가 3줄 이상이면 번호를 그만 부릅니다.
    for i in range(5):
        if call[cnt] in maps[i]:
            j = maps[i].index(call[cnt])
            visited[i][j] = True
    cnt += 1
    # 각 빙고줄을 확인하며 부르는 숫자가 있으면 나온것을 처리하고 다음 숫자로 넘어갑니다.
    
print(cnt)
# 몇 번째 숫자까지 불렀는지 출력해줍니다.