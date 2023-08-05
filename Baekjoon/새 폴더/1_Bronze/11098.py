t = int(input())
for tc in range(t):
    n = int(input())
    mostExpensive = ''
    record = 0
    for _ in range(n):
        price, player = input().split()
        if int(price) > record:
            record = int(price)
            mostExpensive = player
    print(mostExpensive)