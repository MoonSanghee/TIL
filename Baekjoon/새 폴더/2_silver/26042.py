from collections import deque

n = int(input())
line = deque()
answer = [0, 0]
# 주어지는 입력이 몇개인지 받고 줄을 담을 덱을 만들고 최대 줄의 길이와 맨 뒤 사람의 번호를 담을 변수를ㄹ 설정해줍니다.
for _ in range(n):
    code = list(map(int, input().split()))
    # 주어지는 정보를 받아줍니다.
    if code[0] == 1:
        line.append(code[1])
        if answer[0] < len(line):
            answer[0] = len(line)
            answer[1] = line[-1]
        elif answer[0] == len(line):
            answer[1] = min(answer[1], line[-1])
    # 줄이 추가된다면 줄을 서는 학생 정보를 덱에 넣어주고
    elif code[0] == 2:
        line.popleft()
    # 식사 준비가 된다면 맨 앞의 1명을 빼줍니다.

print(*answer)
# 요청된 형식에 맞추어 최대 줄과 그 떄 가장 뒤에 사람의 번호를 출력해줍니다.