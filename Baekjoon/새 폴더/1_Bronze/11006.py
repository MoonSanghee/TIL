tc = int(input())
# 입력받을 테스트케이스의 수를 받아줍니다
for _ in range(tc):
    n, m = map(int, input().split())
    # 닭 다리의 수와 닭의 수를 받아줍니다
    total = m * 2
    # 온전한 경우 다리의 수를 구해줍니다.
    print(total - n, n - m)
    # 다리가 잘린 닭과 잘리지 않은 닭의 수를 출력해줍니다.