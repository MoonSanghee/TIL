# 7-3 문제번호 1193

x = int(input())
a = 0
b = 1
# b는 그 줄의 분수가 가지는 분자 + 분모의 값이다 
c = x
while x > a :
    c -= b
    # c = 0일때 분자 + 분모가 b인 줄의 끝까지 간 것이다.
    a += b
    b += 1
mot = (c - 1) * (-1)
son = b - mot
# print(b)
# if b % 2 == 0:
#     print(f'{mot}/{son}')
# else:
#     print(f'{son}/{mot}')