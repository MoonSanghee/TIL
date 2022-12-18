import sys
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
    # n개의 수를 입력받아 리스트에 넣고
nums.sort(reverse=True)
# 리스트를 내림차순으로 정렬하고
for i in range(n):
    print(nums[i])
    # 차례로 출력해줍니다.