n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
# 영역의 크기와 영역의 가격을 받아줍니다.
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 인접한 4방향을 탐색하기위해 4방향을 설정해줍니다.
result = 5 * 3 * 200
# 꽃이 피는 영역 * 피어나는 꽃의 수 * 최대비용을 비용으로 설정해줍니다

def pick(points):
    global result
    # 세 점을 선택하는 함수입니다.
    if len(points) == 15:
        cost = 0
        for x, y in points:
            cost += maps[x][y]
        result = min(result, cost)
        # 세 점을 골랐다면 비용을 확인해 갱신해줍니다.
        return

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            flag = True
            around = [(i, j)]
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                around.append((nx,ny))
                if (nx, ny) in points:
                    flag = False
                    # 각 영역을 확인하며 씨앗을 심지 못한다면 표시해줍니다. 
            if flag:
                points += around
                pick(points)
                for _ in range(5):
                    points.pop()
                # 씨앗을 심을수 있다면 꽃이 피는 좌표를 리스트에 담고 재귀한 후 꽃이 피는 영역을 빼줍니다.

pick([])
print(result)
# 함수를 실행시키고 나온 결과값을 출력해줍니다.