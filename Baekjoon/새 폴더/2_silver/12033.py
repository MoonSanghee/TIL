t = int(input())
# 테스트 케이스의 수를 받아줍니다.
for tc in range(t):
    items = int(input())
    prices = list(map(int, input().split()))
    # 출력한 모든 가격표를 받아줍니다.
    result = []
    while prices:
        price = prices.pop(0)
        if (price * 4 // 3) in prices:
            result.append(str(price))
            prices.remove((price * 4 // 3))
        # 가격표의 할인전 가격을 계산하여 남은 가격표중에 같은 값이 있다면 
        # 할인된 가격표이므로 리스트에 넣고 할인전 가격은 주어진 리스트에서 지워줍니다.
    print(f'Case #{tc + 1}: {" ".join(result)}')
    # 주어진 양식에 맞춰 출력해줍니다.