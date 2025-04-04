t = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(t):
    n = int(input())
    average = 100001
    price = 100001
    # 맛살이 몇가지인지 받고 평균값과 구매가격을 최대 가격 이상으로 설정해줍니다
    for _ in range(n):
        w, c = map(int, input().split())
        if c / w < average:
            average = c / w
            price = c
        elif c / w == average:
            if c < price:
                price = c
        # 맛살의 무게와 가격을 받고 무게당 가격이 더 싼지 확인하고 같다면 가격이 싼 것으로 갱신해줍니다
    print(price)
    # 최종 구매가격을 출력해줍니다