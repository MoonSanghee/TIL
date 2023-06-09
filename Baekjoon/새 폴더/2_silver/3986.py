n = int(input())
# 단어의 개수를 받아줍니다.
words = [input() for _ in range(n)]
# 단어들을 입력받아 리스트에 넣어줍니다.
count = 0
# 좋은 단어의 개수를 저장할 변수를 지정해줍니다.
for word in words:
    # 모든 단어를 차례대로 순회하여줍니다.
    stack = []
    # 스택이란 이름의 리스트를 만들어줍니다.
    for i in word:
        # 단어의 모든 문자를 순회하며
        if not stack or stack[-1] != i:
            # 스택이 비었거나 가장 뒤에 들어간 문자와 오는 문자가 다르다면
            stack.append(i)
            # 새로 받은 문자를 스택에 넣어주고
        else:
            stack.pop()
            # 두 조건 모두 맞지 않다면 교차하지않고 연결 가능하므로 스택에서 빼줍니다.
    if not stack:
        count += 1
    # 모든 문자를 순회한 후 스택이 비었다면 모든 문자들이 이어졌으니 count 값을 1 더해줍니다. 

print(count)
# 모든 단어를 확인 후 count에 저장된 값을 출력해줍니다.