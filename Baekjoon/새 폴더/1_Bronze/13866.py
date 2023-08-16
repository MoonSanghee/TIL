nums = list(map(int, input().split()))
# 4개의 수를 받아줍니다.
a = max(nums) + min(nums)
b = sum(nums) - a
print(abs(a - b))
# 가장 큰 수와 작은수를 합한 값과 나머지 두 수의 합의 차의 절대값을 출력해줍니다.