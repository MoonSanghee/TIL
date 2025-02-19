n = int(input())
menu = [int(input()) for _ in range(n)]
# 메뉴별로 가격을 받아줍니다
m = int(input())
result = 0
for _ in range(m):
    number = int(input()) - 1
    result += menu[number]
# 주문할 음식의 가격을 더해줍니다
print(result)
# 결과값을 출력해줍니다