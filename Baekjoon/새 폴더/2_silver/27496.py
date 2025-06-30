from collections import deque

n, l = map(int, input().split())
arr = list(map(int, input().split()))
# 주어지는 변수들을 받아줍니다
past = deque()
status = 0
result = 0
# 남은 알코올의 기록을 담을 덱과 현재 알코올 상태, 최적의 상태인 시간을 담을 변수를 설정해줍니다
for i in range(n):
    past.append(arr[i])
    status += arr[i]
    if len(past) > l:
        status -= past.popleft()
    if 129 <= status <= 138:
        result += 1
    # 알코올을 섭취하고 유지 기간이 지난 기록을 빼고 최적의 상태라면 시간을 더해줍니다
print(result)
# 결과를 출력해줍니다