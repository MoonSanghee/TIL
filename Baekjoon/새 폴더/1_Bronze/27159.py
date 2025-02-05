n = int(input())
numbers = list(map(int, input().split()))
# 카드의 개수와 주어지는 카드를 받아줍니다
result = numbers[0]
# 가장 첫번째 카드를 결과에 담아줍니다
for i in range(1, n):
    if numbers[i - 1] + 1 != numbers[i]:
        result += numbers[i]
# 두 번째 카드부터 이전 카드와 연속하지 않아 새 그룹에 포함되는지 확인하고 결과값을 갱신해줍니다
print(result)
# 결과를 출력해줍니다