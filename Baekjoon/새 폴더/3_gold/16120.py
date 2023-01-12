string = input()
stack = []
# 입력받은 문자를 받고 빈 리스트를 만들어줍니다.
for i in string:
    stack.append(i)
    if len(stack) >= 4:
        # 차례대로 스택에 넣고 스택의 길이가 PPAP를 갖출 수 있는지 확인해줍니다.
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            for j in range(3):
                stack.pop()
                # 뒤에서부터 4개를 확인하여 PPAP가 들어왔다면 P로 바꿔주기 위해
                # 나중에 들어간 PAP를 빼줍니다.(pop())

if stack == ['P']:
    print('PPAP')
    # 스택에 P하나만 남았으면 PPAP문자이고
else:
    print('NP')
    # 다른것이 남아있다면 PPAP문자가 아닙니다.