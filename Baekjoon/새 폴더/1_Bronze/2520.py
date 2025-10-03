t = int(input())
# 테스트케이스의 수를 받아줍니다
for _ in range(t):
    blank = input()
    # 공백을 받아줍니다
    ingredients = list(map(int, input().split()))
    topping = list(map(int, input().split()))
    # 반죽과 토핑 변수를 받아줍니다
    result = [ingredients[0] * 2, ingredients[1] * 2, ingredients[2] * 4, ingredients[3] * 16, ingredients[4] * 16 // 9]
    cnt = topping[0] + topping[1] // 30 + topping[2] // 25 + topping[3] // 10
    # 반죽과 토핑으로 만들수있는 팬케이크의 수를 구해줍니다
    pancakes = min(result)
    print(min(pancakes, cnt))
    # 결과를 출력해줍니다