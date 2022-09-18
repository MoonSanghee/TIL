sen = input()
stack = []
open = 0
for i in sen:
    if i == ' ' or i == '<':
        while stack:
            a = stack.pop()
            print(a, end = '')
        if i == '<':
            open = 1
        print(i, end = '')
    elif i == '>':
        print(i, end = '')
        open = 0
    else:
        if open == 0:
            stack.append(i)
        else:
            print(i, end = '')
while stack:
    a = stack.pop()
    print(a, end = '')