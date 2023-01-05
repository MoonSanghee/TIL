n = int(input())
# 몇 번째 수를 구할것인지 받아줍니다.
nums = [0, 1]
# 0번과 1번 피보나치 수를 넣어줍니다.
for i in range(1, n):
    nums.append(nums[i - 1] + nums[i])
    # 그 이후엔 i - 1과 i 인덱스에 위치한 갑을 더한 값을 계속 추가해 줍니다.
print(nums[n])
# 원하는 자리의 수를 출력해줍니다.
