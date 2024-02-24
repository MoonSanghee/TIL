n = int(input())
nums = [0] * 10001
# 선의 개수와 선을 표시할 변수를 설정합니다.
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, y):
        nums[i] = 1
    # n개의 선에서 주어진 범위의 선을 칠하여줍니다.

print(sum(nums))
# 칠해진 선의 영역의 합을 출력해줍니다.