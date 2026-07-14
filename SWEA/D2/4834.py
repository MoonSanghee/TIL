T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    n = int(input())
    a = input()
    # 주어지는 카드의 수와 카드들을 받아줍니다
    cards = [0] * 10
    result = 0
    # 각 카드의 개수와 결과를 담을 변수를 설정해줍니다
    for i in a:
        cards[int(i)] += 1
    # 각 카드가 몇개씩 존재하는지 확인해줍니다
    for i in range(10):
        if cards[i] >= cards[result]:
            result = i
    # 가장 많은 카드를 찾아줍니다
    print(f'#{t + 1} {result} {cards[result]}')
    # 결과를 주어진 양식에 맞게 출력해줍니다