n = int(input())
stack = []
for i in range(n):
    code = list(map(str, input().split()))
    if code[0] == 'push':
        stack.append(code[1])
    elif code[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif code[0] == 'size':
        print(len(stack))
    elif code[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif code[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])