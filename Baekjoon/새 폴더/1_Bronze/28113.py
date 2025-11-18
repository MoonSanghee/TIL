n, a, b = map(int, input().split())

if a < b:
    print("Bus")
elif a == b:
    print("Anything")
else:
    print("Subway")
# 주어진 조건을 통해 어떤 수단을 이용하는게 빠른지 출력해줍니다