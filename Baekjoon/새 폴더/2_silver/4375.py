while True :
    try :
        n = int(input())
    except :
        break

    cnt = 1
    now = 1
    while True:
        if now % n == 0:
            print(cnt)
            break
        now += 10**cnt
        cnt += 1
