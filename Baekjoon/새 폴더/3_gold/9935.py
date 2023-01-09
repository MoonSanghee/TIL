word = input()
d = list(input())
# 전체 단어와 지울 단어를 받아줍니다.
stack = []
# 전체 단어를 순회하며 확인해줄 stack을 만들어줍니다.
for i in range(len(word)):
    stack.append(word[i])
    if stack[-1] == d[-1] and len(stack) >= len(d):
        # 스택의 마지막 문자와 지울 단어의 마지막 문자의 길이가 같고
        # 스택이 지울 단어의 길이와 같거나 킬다면
        if stack[-len(d):] == d:
            # 뒤에서부터 지울 문자의 길이 만큼을 지울 단어와 비교해줍니다.
            for i in range(len(d)):
                stack.pop()
                # 지울 문자의 길이만큼 나중에 들어간 문자들을 빼줍니다.

if stack:
    print(''.join(stack))
    # 스택에 값이 남아있다면 여백없이 스택의 값들을 더해 출력해주고
else:
    print('FRULA')
    # 없다면 요구했던 값을 출력해줍니다.