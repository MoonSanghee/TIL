a, b = map(int, input().split())
# 두 수를 받아줍니다.
multiple = a * b
while b:
    if a > b:
        a, b = b, a
    b %= a
# 유클리드 호제법을 이용하여 최대 공약수를 구해줍니다.
print(multiple // a)
# 최소 공배수를 출력해줍니다