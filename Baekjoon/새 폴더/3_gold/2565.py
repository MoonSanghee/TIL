n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()
# 선의 개수와 현재 위치하고있는 선의 상태를 입력받아줍니다.
# 입력받은 선을 오름차순 정렬해줍니다.
dp = [1] * n
# 각 선의 위치까지 최대 몇개까지 얽히지 않는지 저장해줄 dp를 만들어줍니다.

for i in range(n):
# 각 줄을 확인하며
    for j in range(i):
        if lines[i][1] > lines[j][1]:
        # A전봇대에서 i 이전에 출발하는 모든 선에 대하여
        # i에서 출발하는 선과 겹치지 않는지 확인하고 
            dp[i] = max(dp[i], dp[j] + 1)
            # 겹치지 않는다면 i에서 출발하는 선까지의 최대 겹치지 않는 선의 개수는
            # 현재 dp[i]에 저장되있는 값과 dp[j]에 저장된 값에 1을 더한값중 큰 수로 갱신해줍니다.
print(n - max(dp))
# 모든 전깃줄이 겹치지 않도록하기위해서는 dp에 가장 많은 선이 겹치지 않는 경우의
# 선들은 제외한 모든 선을 없앤 상태이므로 n에서 max(dp)를 빼줍니다.