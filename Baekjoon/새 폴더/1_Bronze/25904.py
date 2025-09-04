n, x = list(map(int, input().split()))
players = list(map(int, input().split()))
# 수의 개수와 내야하는 목소리의 높이를 받고 참가자들의 한계를 받아줍니다
n = 0
while True:
    if players[n] < x:
        print(n + 1)
        break
    else:
        x += 1
        n = (n + 1) % len(players)
    # 참가자가 소리를 못 내는 경우를 찾을때까지 순서를 차례대로 진행하며 내야하는 소리를 1씩 올려줍니다