from collections import deque

s = input()
# 주어지는 괄호를 받아줍니다.

q = deque()
cnt = 0
# 열린 괄호를 담아둘 큐와 추가해야하는 괄호의 개수를 담을 변수를 설정해줍니다.

for i in s:
    if i == '(':
        q.append(i)
        # 열린 괄호라면 큐에 넣어주고
    elif q:
        q.popleft()
        # 닫힌 괄호라면 사용가능한 닫힌 괄호가 있는지 확인하여 있다면 쌍을 지어줍니다.
    else:
        cnt += 1
        # 닫힌 괄호가 없다면 필요한 괄호를 1개 추가해줍니다.

cnt += len(q)
# 남은 괄호의 개수를 더해줍니다.
print(cnt)
# 결과를 출력해줍니다