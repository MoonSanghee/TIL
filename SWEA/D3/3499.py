T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n = int(input())
    cards = list(input().split())
    result = []
    # 주어지는 카드의 수와 최초 나열된 카드를 받고 결과를 담을 변수를 설정해줍니다
    if n % 2:
        for i in range(n // 2):
            result.append(cards[i])
            result.append(cards[i + 1 + n // 2])
        result.append(cards[n // 2])
    else:
        for i in range(n // 2):
            result.append(cards[i])
            result.append(cards[i + n // 2])
    # 카드의 수가 홀수인지 짝수인지를 확인하여 퍼펙트셔플을 실행해줍니다
    result = ' '.join(result)
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다