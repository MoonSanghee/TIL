t = int(input())
# 확인할 테스트 케이스의 수를 받아줍니다.
for _ in range(t):
    n = int(input())
    shop = sorted(list(map(int, input().split())))
    # 상점의 수와 상점이 위치한 정수 좌표를 받고 오름차순으로 정렬해줍니다.
    print((shop[-1] - shop[0]) * 2)
    # 상점들은 한 선 위에 위치하므로 가장 앞에 위치한 상점에서 가장 뒤에 위치한 상점까지의 왕복 거리를 출력해줍니다.