n = int(input())
infos = []
# 회의의 개수를 받고 회의의 정보들을 담을 리스트를 만들어줍니다
for _ in range(n):
    infos.append(list(map(int, input().split())))
infos.sort()
# 회의 정보들을 리스트에 담고 시작시간을 기준으로 오름차순 정렬을 해줍니다

dp = [0] * n
dp[0] = infos[0][2]
# n길이의 dp 리스트를 만들고 첫 인덱스의 값을 회의 정보에 참여하는 사람의 수로 갱신해줍니다
for i in range(1, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + infos[i][2])
# 각 회의를 진행할 경우 인원이 더 참여할 수 있는지를 확인해 값을 갱신해줍니다
print(dp[-1])
# 가장 많은 사람을 수용할때 인원수를 출력해줍니다