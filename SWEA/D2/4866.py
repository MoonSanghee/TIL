T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    code = input()
    keep = list()
    flag = True
    # 주어지는 문자열을 받고 짝을 이루는 괄호를 담아둘 리스트와 괄호의 짝이 모두 맞는지 확인할 변수를 설정해줍니다
    for i in code:
        if i == '{' or i == '(':
            keep.append(i)
        elif i == '}':
            if keep and keep[-1] == '{':
                keep.pop()
            else:
                flag = False
                break
        elif i == ')':
            if keep and keep[-1] == '(':
                keep.pop()
            else:
                flag = False
                break
    # 괄호의 짝이 맞는지 확인해줍니다
    if keep:
        flag = False
    # 짝이 맞지않고 남은 괄호가 있는지 확인해줍니다
    if flag:
        print(f'#{t + 1} 1')
    else:
        print(f'#{t + 1} 0')
    # 결과를 주어진 양식에 맞게 출력해줍니다