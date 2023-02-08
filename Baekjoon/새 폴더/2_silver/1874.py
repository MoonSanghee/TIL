n = int(input())
# 확인할 범위 n을 받아줍니다.
li = []
stack = []
# 숫자를 넣었다 빼는 작업을 할 stack과 기호를 넣어줄 li를 리스트로 만들어줍니다.
cnt = 1
# 숫자를 어디까지 확인하였는지 비교해줄 cnt를 설정해줍니다.
for i in range(1, n + 1):
    num = int(input())
    # n번만큼 수를 입력받으면서
    while cnt <= num:
        stack.append(cnt)
        li.append('+')
        cnt += 1
        # cnt가 num보다 작거나 같다면 cnt에 도달할 때까지 stack에 넣어주고 
        # li에 '+'를 넣어줍니다.
    if stack[-1] == num:
        # 스택의 마지막 값이 입력받은 num과 같다면
        stack.pop()
        li.append('-')
        # 스택의 마지막값을 빼주고 li에 pop을 했다는 의미인 '-'을 추가해줍니다.

if not stack:
    for i in li:
        print(i)
    # 스택이 비었다면 입력되어있는 연산을 차례로 출력해주고
else:
    print('NO')
    # 아니라면 'NO를 출력해줍니다.