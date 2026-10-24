T = int(input())
for tc in range(1, T + 1):
    n = float(input())     
    cnt = 0
    binary = '' 
    while n > 0:
        temp = n * 2        
        binary += str(temp)[0]
        n = temp - int(temp)
        cnt += 1
        if cnt > 12:
            print('#{} {}'.format(tc, 'overflow'))
            break     
    else:        
        print('#{} {}'.format(tc, binary))