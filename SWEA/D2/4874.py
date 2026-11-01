T = int(input())

for tc in range(1, T + 1):
    li = list(input().split())
    stack = []

    result = 0

    for i in li:
        if i.isdigit():
            stack.append(int(i))
        elif i == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
        else:
            if len(stack) < 2:
                result = 'error'
                break
            else:
                n2 = stack.pop()
                n1 = stack.pop()

                if i == '+':
                    stack.append(n1 + n2)
                elif i == '-':
                    stack.append(n1 - n2)
                elif i == '*':
                    stack.append(n1 * n2)
                else:
                    stack.append(n1 // n2)
    
    print(f'#{tc} {result}')