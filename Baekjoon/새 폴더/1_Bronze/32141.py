n, h = map(int, input().split())
cards = list(map(int, input().split()))
# 체력과 카드의 수 그리고 주어지는 카드들을 받아줍니다
for i in range(n):
    h -= cards[i]
    if h < 1:
        print(i + 1)
        break
# 카드의 값만큼 체력을 깎아 0이하가 된다면 몇번째 카드인지 출력해줍니다
else:
    print(-1)
# 0이하로 떨어지지 않는다면 -1을 출력해줍니다