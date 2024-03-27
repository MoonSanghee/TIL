B, C, D = map(int, input().split())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
# 버거, 사이드, 음료의 수를 받고 각 메뉴의 가격을 받아줍니다.
b.sort(reverse = True)
c.sort(reverse = True)
d.sort(reverse = True)
# 각 메뉴를 내림차순으로 정렬해줍니다.
before = 0
after = 0
# 할인 전 가격과 할인 후 가격을 담을 변수를 선언해줍니다.
cnt = min(B, C, D)
# 세트를 몇 개 만들수 있는지 확인해줍니다.
for i in range(cnt):
    price = b[i] + c[i] + d[i]
    before += price
    after += price * 0.9
# 세트 할인이 적용된 가격을 before에 원래 가격을 after에 담습니다.
left = sum(b[cnt:]) + sum(c[cnt:]) + sum(d[cnt:])
before += left
after += left
# 남은 메뉴의 가격을 구해 before와 after에 담아줍니다
print(before)
print(int(after))
# before와 after를 차례대로 출력해줍니다.