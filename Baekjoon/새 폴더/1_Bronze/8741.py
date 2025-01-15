k = int(input())
number = (2 ** k) * (2 ** k - 1) // 2
result = bin(number)[2:]
print(result)
# 주어지는 자릿수를 받고 1부터 2의 k승 - 1까지 합을 구하여 2진수로 변환한 값을 출력해줍니다