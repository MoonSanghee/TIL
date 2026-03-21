T = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(T):
    N, D = map(int, input().split())
    result = 0
    # 우주선의 수와 목적지까지의 거리를 받고 결과를 담을 변수를 설정해줍니다
    for _ in range(N):
        v, f, c = map(int, input().split())
        if v * f / c >= D:
            result += 1
    # 우주선을 순회하며 목적지까지 도달할 수 있는지 확인해줍니다
    print(result)
    # 결과를 출력해줍니다