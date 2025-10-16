n, m = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
# 주어지는 변수를 받아줍니다
if n == 1 or m == 1:
    if sx == ex and sy == ey:
        print("YES")
    else:
        print("NO")
    # 체스판의 가로 혹은 세로의 크기가 1이라면 움직일수 없습니다
elif (sx + ex) % 2 == (sy + ey) % 2:
    print("YES")
else:
    print("NO")
    # 가로와 세로 모두 크기가 1이 아니라면 x + y를 2로 나눈 나머지가 같은 영역은 도달할 수 있습니다