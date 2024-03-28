n = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
# 수의 개수와 수열을 받고 내림차순으로 정렬해줍니다.
result = 0
# 점수를 담을 변수를 선언해줍니다.
for i in range(n - 1):
    score = numbers[i] * numbers[i + 1]
    result += score
    numbers[i + 1] = numbers[i] + numbers[i + 1]
    # 얻을 점수를 구하여 다하고 슬라임의 크기를 바꾸어줍니다.

print(result)
# 최종 획득한 점수를 출력해줍니다.