n = int(input())
numbers = list(map(int, input().split()))
# 수의 개수와 약수를 확인할 수들을 받아줍니다.
result = []

for i in numbers:
    if i == int(i ** 0.5) ** 2:
        result.append(1)
    else:
        result.append(0)
    # 수를 차례대로 확인하며 제곱수라면 리스트안에 결과를 넣어줍니다.
print(*result)
# 결과를 출력해줍니다.