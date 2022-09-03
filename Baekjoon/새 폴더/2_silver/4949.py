while True:
    senten = input()

    if senten == '.':    # 종료 조건
        break
    
    bracket = []
    cnt_break = 0

    for i in senten:
        if i == '(':
            bracket.append(i)
        elif i == ')':
            if len(bracket) == 0:
                cnt_break = 1
                break
            if bracket[-1] == '(':
                bracket.pop()
            else:
                cnt_break = 1
                break
        
        if i == '[':
            bracket.append(i)
        elif i == ']':
            if len(bracket) == 0:
                cnt_break = 1
                break
            if bracket[-1] == '[':
                bracket.pop()
            else:
                cnt_break = 1
                break

    if cnt_break == 0 and bracket == []:
        print('yes')
    else:
        print('no')