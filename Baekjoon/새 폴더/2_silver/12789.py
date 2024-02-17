n = int(input())
numbers = list(map(int, input().split()))
# 수열의 길이와 수열을 받아줍니다.
stack = []
target = 1
# 간식을 받을 수 없는 사람을 차례대로 넣을 스택을 만들고 간식을 받을 번호를 설정해줍니다.
for i in numbers:
    stack.append(i)
    # 수열을 순회하며 위치한 수를 스택에 넣어줍니다.
    while stack and stack[-1] == target:
        stack.pop()
        target += 1
        # 스택이 존재하고 스택의 마지막 값이 타겟과 동일하다면 스택에서 값을 빼고 타겟을 수정해줍니다.

if stack:
    print("Sad")
else:
    print("Nice")
    # 스택에 값이 남았다면 간식을 못 받은 사람이 존재하므로 Sad 없다면 Nice를 출력해줍니다.