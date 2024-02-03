a, b, c = map(int, input().split())
# 세 수를 받아줍니다.
if a+b == c:
    print(f'{a}+{b}={c}')
elif a == b+c:
    print(f'{a}={b}+{c}')
# 두 수를 더해 등호가 성립하는지 확인해줍니다.
elif a-b == c:
    print(f'{a}-{b}={c}')
elif a == b-c:
    print(f'{a}={b}-{c}')
# 두 수를 빼서 등호가 성립하는지 확인해줍니다.
elif a*b == c:
    print(f'{a}*{b}={c}')
elif a == b*c:
    print(f'{a}={b}*{c}')
# 두 수를 곱하여 등호가 성립하는지 확인해줍니다.
elif a/b == c:
    print(f'{a}/{b}={c}')
else:
    print(f'{a}={b}/{c}')
# 두 수를 나누어 등호가 성립하는지 확인해줍니다.