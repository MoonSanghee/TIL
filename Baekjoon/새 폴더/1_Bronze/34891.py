n, m = map(int, input().split())
# 물건의 개수와 박스에 들어가는 물건의 수를 받아줍니다
if n % m:
    print((n // m) + 1)
else:
    print((n // m))
# 필요한 박스의 수를 출력해줍니다