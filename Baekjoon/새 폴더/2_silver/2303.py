n = int(input())
# 사람의 수를 받아줍니다.
numbers = [0 for _ in range(n)]
# 세수의 합 일의 자리를 담을 리스트를 만들어줍니다.
for idx in range(n):
    cards = list(map(int, input().split()))
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                number = (cards[i] + cards[j] + cards[k]) % 10
                if number > numbers[idx]:
                    numbers[idx] = number
    # 각 플레이어의 카드를 임의로 3장 뽑아 일의 자리수가 가장 높은 조합을 구하여 담아줍니다.
big = 0
result = 0
for i in range(n):
    if numbers[i] >= big:
        big = numbers[i]
        result = i + 1
# 가장 큰 일의 자리가 갱신되거나 같은 값이 나오면 사람의 번호를 갱신해줍니다.
print(result)
# 결과를 출력해줍니다.