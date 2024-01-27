n = int(input())
soldiers = list(map(int, input().split()))
# 병사의 수와 군인의 전투력을 받아줍니다.
dp = [1] * n
# 가장 길게 정렬할 수 있는 길이를 담을 dp 리스트를 만들어줍니다.
for i in range(n):
    for j in range(i):
        # 각 자리에서 그 이전 자리들을 차례대로 확인해줍니다.
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[j] + 1, dp[i])
            # 현재 자리까지 정렬할 수 있는 최장 길이를 갱신해줍니다.

print(len(soldiers) - max(dp))
# 몇 명을 빼야하는지 출력해줍니다.