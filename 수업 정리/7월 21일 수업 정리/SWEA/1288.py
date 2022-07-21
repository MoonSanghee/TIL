t = int(input())
for i in range(t):
    a = int(input())
    b = []
    c = 0
    d = a
    check_box = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while b != check_box:
        b += str(d)
        d += a
        b = sorted(list(set(b)))
        c += 1
    print(f'#{i+1}', end = " ")
    print(a * c)
    # 몇 번 반복했을때를 묻는것이 아니라 몇 번 양을 셌을 때를 묻고있다.