T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n = int(input())
    x = list(map(int, input().split()))
    result = 10000
    # 주어지는 경로의 수와 경로를 받고 결과를 설정해줍니다
    for i in range(1, n - 1):
        new = x[:i] + x[i + 1:]
        cost = 0
        for j in range(1, n - 1):
            cost += abs(new[j] - new[j - 1])
        result = min(result, cost)
    # 임의의 한 자리를 방문하지않는 모든 경우를 확인하며 최단 이동경로를 찾아줍니다
    print(result)
    # 결과를 출력해줍니다