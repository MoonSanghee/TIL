n, k = map(int, input().split())
numbers = list(map(int, input().split()))
# n과 k를 받고 수열을 받아줍니다.
result = 0
# 결과를 담을 변수를 설정해줍니다.

for i in range(k):
    result -= i
# k개의 수를 고르므로 k 미만의 정수만큼의 점수가 차감됩니다.

numbers.sort(reverse=True)
for i in range(k):
    result += numbers[i]
# 수열을 내림차순으로 정렬하고 k개의 큰수를 골라줍니다.

print(result)
# 결과를 출력해줍니다.