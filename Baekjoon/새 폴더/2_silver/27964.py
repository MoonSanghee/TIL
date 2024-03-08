n = int(input())
topping = list(map(str, input().split()))
# 토핑의 종류와 주어지는 토핑을 받습니다.
cheese = set()
# 치즈를 담을 세트 자료구조를 만들어줍니다.
for i in topping:
    if i[-6:] == "Cheese":
        cheese.add(i)
        # 치즈로 끝나는 재료라면 추가해줍니다.

if len(cheese) >= 4:
    print('yummy')
else:
    print('sad')
    # 4종류 이상인지 확인하고 결과를 출력해줍니다.