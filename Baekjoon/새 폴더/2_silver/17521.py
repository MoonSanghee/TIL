n, w = map(int, input().split())
price = [int(input()) for _ in range(n)]
# 총 거래일과 시작 자본을 받고 거래일동안의 시세를 받아줍니다
cnt = 0
# 코인의 개수를 담을 변수를 설정해줍니다
for i in range(n - 1):
    if price[i] <= price[i + 1]:
        cnt += w // price[i]
        w %= price[i]
        # 다음날 코인의 가격이 오르거나 유지된다면 최대한 많은 코인을 구매합니다
    else:
        w += cnt * price[i]
        cnt = 0
        # 코인의 가격이 내릴거라면 모든 코인을 팔아서 현금으로 만들어줍니다

w += cnt * price[n - 1]
# 마지막 거래일 이후 남은 코인을 모두 현금으로 바꾸어줍니다
print(w)
# 결과를 출력해줍니다