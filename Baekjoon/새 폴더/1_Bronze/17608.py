n = int(input())
# 막대기의 개수를 입력 받습니다.
stack = []
# 보이는 막대기를 넣어줄 리스트를 만들어줍니다.
result = 1
# 최소 1개의 막대는 보이니 보이는 막대의 개수를 1로 설정해줍니다.
for _ in range(n):
    stack.append(int(input()))
    # 막대가 위치한 순서대로 스택에 넣어줍니다.
m = stack[-1]
# 가장 뒤의 막대 길이를 기준으로잡아줍니다.
for i in range(len(stack)-1, -1, -1):
    if stack[i] > m:
        result += 1
        m = stack[i]
# 막대를 뒤에서부터 확인하여 길이가 이전까지 본 막대의 길이보다 크다면 
# 보이는 막대를 하나 증가시키고 보이는 가장 긴 막대의 길이를 갱신해줍니다.
print(result)
# 보이는 막대의 길이를 출력해줍니다.