t = int(input())
sides = [[0,1,2,3],[4,5,6,7],[0,1,4,5],[2,3,6,7],[0,2,4,6],[1,3,5,7]]
# 테스트케이스의 수를 받고 정육면체의 여섯 면을 리스트에 담아줍니다
for _ in range(t):
    points = sorted(list(map(int, input().split())))
    if points in sides:print('YES')
    else:print('NO')
    # 주어지는 점들을 정렬하여 정육면체의 면에 존재하는지 확인해줍니다