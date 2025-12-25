total = 0
# 총 금액을 담을 변수를 설정해줍니다
n = int(input())
# 지폐의 수를 받아줍니다
for _ in range(n):
    x, y = map(int, input().split())
    if x == 136:
        total += 1000
    elif x == 142:
        total += 5000
    elif x == 148:
        total += 10000
    else:
        total += 50000
# 지폐의 크기를 확인하여 금액을 더해줍니다
print(total)
# 결과를 출력해줍니다