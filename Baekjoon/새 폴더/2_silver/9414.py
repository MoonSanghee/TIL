t = int(input())
# 테스트 케이스가 몇 개 주어지는지 받아줍니다
for tc in range(t):
    price = []
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            price.append(n)
        # 테스트 케이스 단위로 주어지는 땅의 가격을 모두 리스트에 담아줍니다
    price.sort(reverse=True)
    result = 0
    # 담은 땅의 가격을 내림차순으로 정렬하고 땅 구매비용을 담을 변수를 설정해줍니다
    for i in range(len(price)):
        result += 2 * (price[i] ** (i + 1))
        if result > 5 * 10 ** 6:
            print("Too expensive")
            break
        # 땅 구매비용을 갱신하며 제한 금액을 넘어가면 주어진 출력을하고 반복을 멈추어줍니다
    else:
        print(result)
        # 반복이 끝까지 멈추지않았다면 최소 구매비용을 출력해줍니다