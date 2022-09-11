# 백준 4375
while True:
    try:
        n = int(input())
        a = '1'
        while int(a) % n:
            a += '1'
        print(len(a))
    except:
        break
# 여러번의 입력을 하는 try, exept문 활용