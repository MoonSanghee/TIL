word = input()
# 괄호를 입력받아줍니다.
l = []
result = 0
n = 1
# 최종 값과 현재까지 연산 값을 저장할 변수, 괄호의 값을 확인할 리스트를 지정하여줍니다.

for i in range(len(word)):
    # 각 괄호를 확인하며
    if word[i] == '(':
        l.append('(')
        n *= 2
    elif word[i] == '[':
        l.append('[')
        n *= 3
    # 열린 괄호라면 주어진 값만큼 곱해주고
    elif word[i] == ')':
        if not l or l[-1] != '(':
            result = 0
            break
        if word[i-1] == '(':
            result += n
        l.pop()
        n //= 2
    elif word[i] == ']':
        if not l or l[-1] != '[':
            result = 0
            break
        if word[i-1] == '[':
            result += n
        l.pop()
        n //= 3
    # 닫힌 괄호라면 해당 괄호로 닫을 차례가 맞는지 확인하고 
    # 열린 직후 닫힌 경우에만 값을 더해줍니다.
    # 각 괄호를 닫았다면 그 괄호가 가지는 수만큼 나누어주고 l에서 괄호를 빼줍니다.
if l:
    result = 0
# 괄호가 남아있다면 결과를 0으로 바꾸어줍니다.

print(result)
# 결과에 저장된 값을 출력해줍니다.