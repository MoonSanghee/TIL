while True:
    sen = input()

    if sen == '.':
        break

    bracket = []
    cnt = 0

    for i in sen:
        if i == '(' or i == '[':
            bracket.append(i)
        elif i == ')':
            if len(bracket) == 0:
                cnt = 1
                break    
            if bracket[-1] == '(':
                bracket.pop()
            else:
                cnt = 1
                break
        elif i == ']':
            if len(bracket) == 0:
                cnt = 1
                break    
            if bracket[-1] == '[':
                bracket.pop()
            else:
                cnt = 1
                break

    if len(bracket) == 0 and cnt == 0:
        print('yes')
    else:
        print('no')