t = int(input())
for tc in range(t):
    command = input()
    left, right = [], []
    for i in command:
        if i == '<':
            if left:
                l = left.pop()
                right.append(l)
        elif i == '>':
            if right:
                l = right.pop()
                left.append(l)
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    right = right[::-1]
    for i in right:
        left.append(i)

    print(''.join(left))