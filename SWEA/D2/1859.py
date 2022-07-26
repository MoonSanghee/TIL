import sys

sys.stdin = open("1859_input.txt", "r")

tset_case = int(input())

for i in range(tset_case):
    days =int(input())
    price = list(map(int, input().split()))
    earn_money = 0
    sell_price = 0
    buy_price = 0
    for j in range(len(price) - 1):
        if price[days - 1 - j] > price[days -2 -j]:
            if sell_price < price[days - 1 - j]:
                sell_price = price[days - 1 - j]
            buy_price = price[days - 2 - j]
        elif price[days - 2 - j] > price[days -1 -j]:
            buy_price = price[days - 2 - j]
        if buy_price >= sell_price:
            earn_money += 0
        else:
            earn_money += (sell_price - buy_price)
    print(f'#{i + 1} {earn_money}')