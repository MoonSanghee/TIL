t = int(input())
for tc in range(1, t + 1):
    lst = []
    maxi = 0
    for _ in range(5):
        a = str(input())
        lst.append(a)
        if len(a) > maxi:
            maxi = len(a)
    for i in range(5):
        if len(lst[i]) < maxi:
            lst[i] += '*' * (maxi - len(lst[i]))
    
    result = ''
    for i in range(maxi):
        for j in range(5):
            if lst[j][i] != '*':
                result += lst[j][i]
    
    print(f'#{tc} {result}')