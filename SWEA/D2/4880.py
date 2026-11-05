T = int(input())

def splitCards(start, end):
    if start == end:
        return start
    first = splitCards(start, (start + end) // 2)
    second = splitCards(((start + end) // 2) + 1, end)
    return game(first, second)

def game(x, y):
    if (cards[x] % 3) + 1 == cards[y]:
        return y
    else:
        return x

for tc in range(1, T + 1):
    n = int(input())
    cards = list(map(int, input().split()))
    
    print(f'#{tc} {splitCards(0, n - 1) + 1}')