n, m = map(int, input().split())
# 영역의 크기를 받아줍니다.
space = [list(map(int, input().split())) for _ in range(n)]
check = [[[1000] * 3 for _ in range(m)] for _ in range(n)]
# 각 영역을 지날때 필요한 비용을 받아주고 영역의 각 자리마다 3개 방향에서 온 값을 담을 리스트를 만들어줍니다.
# 사이즈가 최대 6 * 6이고 각 영역을 지나는 최대 비용은 100이므로 600이상인 1000으로 값을 설정해주었습니다.

for i in range(m):
    for j in range(3):
        check[0][i][j] = space[0][i]
# 첫 줄의 영역에 도달하는 방법은 한 가지 방법뿐이므로 세 방향 모두 첫 칸의 비용으로 갱신해줍니다.

for i in range(1, n):
    for j in range(m):
        for k in range(3):
            if (j == 0 and k == 2) or (j == m - 1 and k == 0):
                continue
            # 각 영역의 3개 구역을 확인하며 첫 영역은 왼쪽에서 올 수 없고
            # 마지막 영역은 오론쪽에서 값이 올 수 없으니 continue를 이용해서 확인하지 않도록 합니다.
            for l in range(3):
                if k == l:
                    continue
                # 같은 방향에서 갈 수 없으니 내려온 방향과 진행 방향이 같다면 넘겨줍니다.
                check[i][j][k] = min(check[i][j][k], check[i - 1][j - k + 1][l] + space[i][j])
                # 각 영역의 값과 내려가는 값을 확인하여 갱신해줍니다.

result = 1000
for x, y, z in check[-1]:
    result =  min([result, x, y, z])
print(result)
# 각 영역의 마지막 칸을 확인하여 최소비용을 구하고 값을 출력해줍니다.