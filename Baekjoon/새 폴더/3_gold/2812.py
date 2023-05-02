n, k = map(int, input().split())
# 숫자의 자리수와 뺄 수자의 개수를 지정해줍니다.
length = n - k
num = input()
# 남은 자릿수와 수를 입력받아줍니다.
stack = []
# 다음 오는 수가 더 큰지 확인하기 위해 매 자리수를 넣어줄 스택을 만들어줍니다.
for i in range(n):
    while k > 0 and stack and stack[-1] < num[i]:
        # 수를 더 빼줄수 있고 스택에 값이 있으며 스택의의 가장 뒤 자리수가 num[i]보다 작다면 
        stack.pop()
        k -= 1
        # 스택에 저장된 값을 빼주고 1개의 수를 빼준것을 표시해줍니다.
    stack.append(num[i])
    # 스태게 각 자리수를 넣고

print(''.join(stack[:length]))
# 스택의 값들을 합쳐 하나의 수로 만들어부터 앞자리부터 원하는 길이만큼으로 값을 정해줍니다.