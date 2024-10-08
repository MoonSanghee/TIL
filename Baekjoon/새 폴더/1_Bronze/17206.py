n = int(input())
numbers = list(map(int, input().split()))
# 수의 개수와 주어지는 수를 받아줍니다.

result = [0] * 100000
for i in range(1, 100000):
    result[i] = result[i - 1]
    if i % 3 == 0 or i % 7 == 0:
        result[i] += i
# 주어지는 수의 가장 큰 값이 8만이므로 8만 이하의 모든 수를 확인하여 그 수보다 
# 작은 3과 7의 배수를 합한값을 담아줍니다.
for i in numbers:
    print(result[i])
    # 주어진 수들 이하의 3과 7의 배수 합을 구해줍니다.