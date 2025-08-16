from collections import deque
t = int(input())
# 테스트케이스의 수를 받아줍니다
for tc in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    # 가격의 개수와 주어지는 가격을 받아줍니다
    sales = []
    used = deque()
    # 세일 가격을 담을 리스트와 나오지않은 세일 전 가격을 담을 덱을 만들어줍니다
    for price in prices:
        if not used:
            sales.append(price)
            used.append((price * 4) // 3)
        else:
            if price == used[0]:
                used.popleft()
            else:
                sales.append(price)
                used.append((price * 4) // 3)
            # 주어진 가격을 순회하며 세일 전 가격이 비었거나 가격이 세일 전 가격의 가장 작은 값보다 작다면
            # 세일 후의 가격이고 아니라면 세일 전의 가격입니다
    result = ' '.join(map(str, sales))
    print(f"Case #{tc + 1}: {result}")
    # 주어지는 양식에 맞추어 결과를 출력해줍니다