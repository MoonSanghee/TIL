while True:
    try:
        s, t = map(str, input().split())
        cnt = 0
        for c in t:
            if c == s[cnt]:
                cnt += 1
                if cnt == len(s):
                    print('Yes')
                    break
        else:
            print('No')
    except:
        break
# try, except을 활용하여 입력의 횟수가 정해지지 않은 경우를 해결하였습니다.
# t를 순서대로 s의 문자를 가지고있는지 확인하고 S의 모든 문자를 차례에 맞게 가지고 있는지 확인하였습니다.