n = int(input())
directions = input()
# 지도의 크기와 이동 방향을 받아줍니다
result = 0
# 선물을 놓아야하는 구역의 수를 담을 변수를 정해줍니다
for i in range(n - 1):
    if directions[i] == 'E' and directions[i + 1] == 'W':
        result += 1
    # E와 W가 마주하고있다면 두 구역을 반복이동하므로 그 곳에 도착한다면 벗어나지 않으므로 선물을 놓아줍니다 
print(result)
# 놓아야하는 선물의 최소개수를 출력해줍니다