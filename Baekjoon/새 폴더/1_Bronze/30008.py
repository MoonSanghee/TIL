n, k = map(int, input().split())
ranks = list(map(int, input().split()))
# 주어지는 변수들을 받아줍니다
for i in ranks:
    glade = (i * 100) // n
    # 백분위를 확인해줍니다
    if glade <= 4:
        print(1, end = ' ')
    elif glade <= 11:
        print(2, end = ' ')
    elif glade <= 23:
        print(3, end = ' ')
    elif glade <= 40:
        print(4, end = ' ')
    elif glade <= 60:
        print(5, end = ' ')
    elif glade <= 77:
        print(6, end = ' ')
    elif glade <= 89:
        print(7, end = ' ')
    elif glade <= 96:
        print(8, end = ' ')
    else:
        print(9, end = ' ')
    # 등급을 출력해줍니다