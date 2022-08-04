ball = [1, 0, 0]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    x = x - 1
    y = y - 1    
    if ball[x] == 1:
        ball[x] = 0
        ball[y] = 1
    elif ball[y] == 1:
        ball[y] = 0
        ball[x] = 1

print(ball.index(1) + 1)