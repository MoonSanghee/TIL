s = list(input())
stack = []
result = ''
# 주어지는 입력을 받고 뒤집히는 연산을 담을 리스트와 결과값을 담을 변수를 설정해줍니다
for i in s:
    if i.isalpha():
        result += i
    # 연산자가 아닌 알파벳이라면 결과에 바로 추가해줍니다
    elif i == '(':
        stack.append(i)
    # 여는 괄호라면 바로 스탯에 담아줍니다
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] =='/'):
            result += stack.pop()
        stack.append(i)
    # 곱셈이나 나눗셈이라면 이전의 곱셈이나 나눗셈 전까지 덩어리를 계산하므로 
    # 스택에서 곱셈이나 나눗셈이 나올때까지 빼서 결과에 더한후 마지막에 스택에 기호를 넣어줍니다
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(i)
    # 곱셈이나 나눗셈이 아니고 덧셈이나 뺄셈이라면 닫힘 기호가 나오기전까지 연산을 계속하므로 
    # 스택의 기호를 차례대로 결과에 더한 후 기호를 스택에 넣어줍니다
    else:
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    # 닫힘 기호라면 열림기호까지의 연산을 진행하므로 열림 기호가 나올때까지 스택의 연산을 빼서 결과에 더해줍니다 
    print(stack, result)

while stack:
    result += stack.pop()
# 스택에 남아있는 연산이 있는지 확인하여 결과에 더해줍니다
print(result)
# 결과를 출력해줍니다