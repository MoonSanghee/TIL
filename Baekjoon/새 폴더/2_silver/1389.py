n, m = map(int, input().split())
# 사람의 수와 관계의 수를 입력받아줍니다.

friends = [[n]*(n + 1) for _ in range(n + 1)]
# 모든 사람간의 관계를 표시할 그래프를 만들어줍니다.

for _ in range(m):
    a, b = map(int, input().split())
    friends[a][b] = 1
    friends[b][a] = 1
    # 입력받은 두 사람이 친구 관계라면 바로 아는 사이이므로 1단계거쳐 친구라고 입력받아줍니다.

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
               friends[i][j] = 0
            # i와 j값이 같다면 자신 스스로와의 관계이므로 0을 입력해줍니다.
            else:
               friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])
            # 본인이 아닌 사람과의 관계는 플로이드-워셜 알고리즘 알고리즘을 통해
            # 각 자리의 최소값을 갱신해줍니다.
total = n * 6
now = 0
# 두 사람 사이 최대 관계 비용은 6이고 n - 1 만큼 있을수 있으므로 한 사람이 모든
# 사람을 아는데 필요한 최대 관계 비용은 n * 6 보다 작으므로 최대 비용으로 설정해줍니다.

for i in range(1, n + 1):
    if sum(friends[i]) < total:
        total = sum(friends[i])
        now = i
        # 각 사람이 가지는 관계 비용이 현재 저장된 값보다 작다면 비용을 갱신해주고
        # 어떤 사람이 인지 표시해줍니다.
print(now)
# 가장 적은 비용으로 모두와 관계를 가지는 사람을 출력해줍니다.