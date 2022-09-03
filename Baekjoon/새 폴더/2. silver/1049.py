buy, case = list(map(int, input().split()))
s = []
e = []
for _ in range(case):
    pack, each = list(map(int, input().split()))
    s.append(pack)
    e.append(each)
if min(s) > min(e) * 6:
    print(buy * min(e))
else:
    if buy % 6 == 0:
        print(min(s) * (buy // 6))
    else:
        price = min(s) * (buy // 6)
        if min(e) * (buy % 6) > min(s):
            price += min(s)
        else:
            price += min(e) * (buy % 6)
        print(price)
        # 들여쓰기 주의하자!!!
