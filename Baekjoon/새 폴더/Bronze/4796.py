case = 0
while True :
    case += 1
    numbers = list(map(int, input().split()))
    can, days, vaca = numbers
    if sum(numbers) == 0:
        break
    cnt = 0
    while vaca != 0:
        if vaca >= days:
            vaca -= days
            cnt += can
        else:
            if vaca < can:
                cnt += vaca
                vaca = 0
            else:
                cnt += can
                vaca = 0
    print(f'Case {case}: {cnt}')