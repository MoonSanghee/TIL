from collections import deque

n, k = map(int, input().split())
nums = deque()

for i in range(n):
    nums.append(str(i + 1))
# 1부터 n개의 정수를 deque에 넣어줍니다.
result = []
# 순열을 저장할 빈 리스트를 만들어줍니다

for _ in range(n):
    for i in range(k):
        passed = nums.popleft()
        nums.append(passed)
    # k번만큼 덱에서 먼저 들어간 값을 뒤로 보내고
    save = nums.pop()
    result.append(save)
    # 가장 뒤의 수를 빼서 리스트에 넣어줍니다.
saved = '<' + ', '.join(result) + '>'
# saved = f'<{", ".join(result)}>'로 표현 가능합니다.
# 리스트의 값을 모아줍니다.
print(saved)