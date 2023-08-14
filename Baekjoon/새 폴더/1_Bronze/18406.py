n = input()
nums = list(map(int, n))
# 수를 받아 자리수별로 나누어 리스트로 만들어줍니다.
if sum(nums[:len(nums)//2]) == sum(nums[len(nums)//2::]):
    print('LUCKY')
    # 앞의 절반과 뒤의 절반의 합이 같다면 'LUCKY'
else:
    print('READY')
    # 다르다면 'READY'를 출력해줍니다.