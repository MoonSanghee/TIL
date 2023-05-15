n = int(input())
nums = list(map(int, input().split()))
# 주어진 길이의 수열을 입력 받아줍니다.
dp1 = [1] * n
dp2 = [1] * n
# 증가하는 수열과 감소하는 수열이 연속되는 길이를 입력해줄 dp 리스트를 2개 만들어줍니다.

for i in range(1, n):
    # 1번 인덱스에 위치한 값부터
    if nums[i] <= nums[i - 1]:
        dp1[i] = max(dp1[i], dp1[i - 1] + 1)
    # 각 인덱스에 위치한 값이 이전에 위치한 인덱스 값 이상이면
    # dp1[i]를 현재 값과 이전 dp 인덱스 값에 1을 더한값을 비교하여 큰 값으로 바꾸어줍니다.
    if nums[i] >= nums[i - 1]:
        dp2[i] = max(dp2[i], dp2[i - 1] + 1)
    # 각 인덱스에 위치한 값이 이전에 위치한 인덱스 값 이하이면
    # dp2에 값을 확인하고 갱신하여줍니다.

print(max(max(dp1), max(dp2)))
# dp1의 가장 긴 값과 dp2의 가장 긴 값을 비교하여 큰 값을 출력해줍니다.