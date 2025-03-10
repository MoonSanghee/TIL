n = int(input())
stones = list(map(int, input().split()))
# 주어지는 돌의 개수와 돌들의 무게를 받아줍니다
left = stones[0]
right = stones[1]
for i in range(2, n):
    if left <= right:
        left += stones[i]
    else:
        right += stones[i]
diffrence = abs(right - left)
# 돌을 차례대로 주어진 규칙에 맞게 저울에 양 측에 놓아 무게 차이를 구해줍니다

cnt = 0
for i in [100, 50, 20, 10, 5, 2, 1]:
    if diffrence // i:
        cnt += diffrence // i
        diffrence %= i
print(cnt)
# 무거운 추부터 확인하여 몇 개의 추가 필요한지 구하여 출력해줍니다