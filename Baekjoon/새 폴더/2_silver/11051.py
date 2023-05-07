n, k = map(int, input().split())
# 두 수 n, k를 받아줍니다.
num = n - k
result = 1
for i in range(k, n):
    result *= (i + 1)
# result에 n팩토리얼을 계산하고 k 팩토리얼을 나눠줍니다.

for i in range(num):
    result //= (i + 1)
# result에 n - k 팩토리얼을 나누어줍니다.
print(result%10007)
# result값을 10007로 나눈 나머지를 출력하여줍니다.