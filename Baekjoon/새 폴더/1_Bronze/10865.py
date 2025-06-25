n, m = map(int, input().split())
# 주어지는 학생의 수와 관계의 수를 받아줍니다
graph = [0] * (n + 1)
# 학생의 친구를 담을 변수를 설정해줍니다
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += 1
    graph[b] += 1
# 친구인 두 학생을 받고 친구의 수를 더해줍니다
for i in range(1, n + 1):
    print(graph[i])
    # 차례대로 학생들이 몇명의 친구를 가지고있는지 출력해줍니다