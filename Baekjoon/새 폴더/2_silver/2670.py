n = int(input())
# 수의 개수를 받아줍니다.
nums = [float(input()) for _ in range(n)]
# 리스트에 수의 개수만큼 소수를 받아줍니다.
for i in range(1, n):
    nums[i] = max(nums[i], nums[i] * nums[i - 1])
    # 1번 인덱스부터 이전 소수와 곱이 더 커지는 경우 값을 갱신해줍니다.

print('%0.3f' % max(nums))
# 리스트에서 가장 큰 값을 소수점 3째 자리까지 출력해줍니다.