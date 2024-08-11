from collections import deque

n = int(input())
# 수열의 길이를 받아줍니다.
skills = list(map(int,input().split()))
skills.reverse()
# 사용한 기술을 차례로 받아 순서를 뒤집어줍니다.
stack = [i + 1 for i in range(n)]
q = deque()
# 만들어진 결과를 리스트로 받고 과정을 확인해 담을 q를 만들어줍니다.
for i in range(n):
    x = stack[i]
    if skills[i] == 1:
        q.appendleft(x)
    elif skills[i] == 2:
        q.insert(1, x)
    else:
        q.append(x)
    # 사용한 스킬을 확인하여 알맞은 방법으로 덱에 값을 추가하여줍니다.

print(*q)
# 결과물을 출력해줍니다.