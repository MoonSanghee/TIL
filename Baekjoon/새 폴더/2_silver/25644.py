n = int(input())
price = list(map(int, input().split()))
# 주어질 거래예정일과 거래가격을 받아줍니다.
high, result = 0, 0
# 가장 높은 가격과 가장 큰 이득을 본 가격을 담을 변수를 만들고 값을 0으로 설정해줍니다.
for i in range(n - 1, -1, -1):
    high = max(high, price[i])
    result = max(result, high - price[i])
    # 가장 마지막날 가격부터 가장 높은 가격인지 확인하고 갱신해준 다음
    # 현재 가격에서 가장 높은 가격에 팔았을때 차익을 비교하여 수익을 비교하고 갱신해줍니다. 

print(result)
# result에 담긴 가장 큰 수익을 출력해줍니다.