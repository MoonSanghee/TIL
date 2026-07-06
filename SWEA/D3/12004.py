T = int(input())

for t in range(T):
    n = int(input())
    flag = False

    for i in range(1, 10):
        if n % i == 0 and n // i <= 9:
            flag = True
            break
    
    if flag:
        print(f'#{t + 1} Yes')
    else:
        print(f'#{t + 1} No')