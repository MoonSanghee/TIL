n, k = map(int, input().split())
# 주어지는 두 수를 받아줍니다
result = ''
for i in range(k - 1):
    result += '1'
result += str(n)
# k - 1길이만큼 1을 채우고 마지막에 n을 붙여줍니다
print(result)
# 결과를 출력해줍니다