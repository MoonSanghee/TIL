n = int(input())
numbers = list(map(int, input().split()))
result = max(numbers) * min(numbers)
print(result)
# n개의 정수를 약수로 가지는 수이므로 가장 큰 값과 가장 작은 값을 
# 곱한 결과가 구하고자하는 정수가 됩니다.