card, max_card = map(int, input().split())
cards = list(map(int, input().split()))

result = 0 

for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(1 + j, len(cards)):
            sum = cards[i] + cards[j] + cards[k]
            if result < sum <= max_card:
                result = sum
print(result)