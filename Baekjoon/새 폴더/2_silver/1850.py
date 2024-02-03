def gcd(x,y):
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y
#유클리드 호제법으로 공약수를 구해줍니다.

A, B = map(int, input().split())
print('1' * gcd(A, B))