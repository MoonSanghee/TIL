T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())

    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    result = '?'

    if a == b:
        if A == B:
            result = '='
    elif a > b:
        for i in B:
            if i not in A:
                break
        else:
            result = '>'
    else:
        for i in A:
            if i not in B:
                break
        else:
            result = '<'
    
    print(result)