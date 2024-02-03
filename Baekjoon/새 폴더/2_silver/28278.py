import sys
input = sys.stdin.readline

t = int(input())
stack = []
# 입력받을 명령의 수와 사용할 스택을 만들어줍니다.
for _ in range(t):
    key = input().rstrip()
    # 입력 명령을 받아줍니다.
    if len(key) > 1:
        stack.append(int(key[2:]))
        # 길이가 1이 넘는다면 스택에 값을 추가하는것이므로 1과 공백 이후를 정수형으로 스택에 넣어줍니다.
    elif key == '2':
        if stack:
            x = stack.pop()
            print(x)
        else:
            print(-1)
    elif key == '3':
        print(len(stack))
    elif key == '4':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    # 명령어를 확인하여 주어진 명령을 실행합니다.