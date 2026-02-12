n = int(input())
result = 'AKARAKA'
# 주어지는 정술를 받아줍니다
if n == 1:
    print(result)
else:
    result += "RAKA" * (n - 1)
    print(result)
# 결과를 출력해줍니다