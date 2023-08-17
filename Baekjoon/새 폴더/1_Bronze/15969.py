n = int(input())
# 학생의 수를 받아줍니다.
nums = sorted(list(map(int, input().split())))
# 성적을 받아 정렬해줍니다.
print(nums[-1] - nums[0])
# 최고점과 최저점의 차를 출력해줍니다.