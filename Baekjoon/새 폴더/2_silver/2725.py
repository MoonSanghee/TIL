def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)
# (0,0)과 한 점만 지나는 선은 기울기가 같은 다른 점이 없는 점이므로
# 최대 공약수를 구하는 함수를 만들어줍니다.

points = [0 for _ in range(1001)]
points[1] = 3
# 주어지는 영역의 최대크기가 1000이므로 1001사이즈의 points리스트를 만들고 
# points[1]을 3으로 갱신해줍니다.

for i in range(2, 1001):
    cnt = 0
    for j in range(1, i + 1):
        if i == j:
            continue
            # i와 j가 같으면 여러개의 점을 지날수밖에 없으므로 continue로 넘겨줍니다.
        if gcd(i, j) == 1:
            cnt += 2
        # 확인한 두 수의 최대 공약수가 1이라면 i와 j가 같은 직전을 기준으로 대칭한 모양이므로
        # cnt 값을 2 증가시켜줍니다.
    points[i] = points[i - 1] + cnt
    # points[i] 값을 갱신해줍니다.

t = int(input())

for tc in range(t):
    n = int(input())
    print(points[n])
    # 테스트 케이스의 수를 받고 points에 담긴 값을 출력해줍니다.