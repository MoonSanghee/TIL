t = int(input())
for _ in range(t):
    number = int(input())
    price = [25, 10, 5, 1]
    coin = []
    for i in range(4):
        coin.append(number // price[i])
        number %= price[i]
    print(*coin)