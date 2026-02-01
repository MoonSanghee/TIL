n, m = map(int, input().split())
cards = [int(input()) for _ in range(n)]
# 학생의 수와 카드의 수, 학생들이 가지고있는 카드의 수를 받아줍니다
for i in range(1, m + 1):
    for j in range(n - 1):
        if cards[j] % i > cards[j + 1] % i:
            cards[j],cards[j + 1] = cards[j + 1], cards[j]
# 카드를 교환해야하는지 확인하여 교환을 진행해줍니다
for i in cards:
    print(i)
# 학생들이 가진 카드를 차례대로 출력해줍니다