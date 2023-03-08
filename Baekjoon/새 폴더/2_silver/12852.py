from collections import deque

n = int(input())
visited = set()
q = deque()
q.append([n])
# 방문처리를 할 set를 만들어주고 덱에 주어진 정수가 들어간 리스트를 넣어줍니다.

while q:
    li = q.popleft()
    num = li[-1]
    # li의 마지막 값을 num이라는 변수로 저장해줍니다.
    if num == 1:
        print(len(li) - 1)
        print(*li)
        break
    # 마지막 연산 결과 1에 도달하였다면 길이에서 1을 뺸 값이 연산 횟수
    # 리스트의 값이 연산 과정이므로 차례대로 출력해줍니다.
    if num%3 == 0 and num//3 not in visited:
        q.append(li + [num // 3])
        visited.add(num)
        # num이 3으로 나누어떨어지고 방문한 적 없다면 li리스트에 num을 3으로 
        # 나눈 값을 더해주고 num을 방문처리 해주고 덱에 리스트를 넣어줍니다.
    if num%2 == 0 and num//2 not in visited:
        q.append(li + [num // 2])
        visited.add(num)
        # num이 2로 나누어떨어지고 방문한 적 없다면 li리스트에 num을 3으로 
        # 나눈 값을 더해주고 num을 방문처리 해주고 덱에 리스트를 넣어줍니다.
    if num - 1 not in visited:
        q.append(li + [num - 1])
        visited.add(num - 1)
        # num보다 1 작은 값에 방문한 적 없다면 방문처리하고 덱에 넣어줍니다.