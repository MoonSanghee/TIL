t = int(input())
# 테스트케이스의 개수를 받아줍니다
for _ in range(t):
    n, m = map(int, input().split())
    result = 0
    # 주어지는 상금과 스티커의 종류를 받아줍니다
    prizes = [list(map(int, input().split())) for _ in range(n)]
    coupons = list(map(int, input().split()))
    # 상금과 쿠폰의 정보를 받아줍니다
    for info in prizes:
        cnt = 100
        for i in range(info[0]):
            cnt = min(cnt, int(coupons[info[i + 1] - 1]))
        result += cnt * info[-1]
        # 쿠폰을 통해 받을수있는 상금을 결과에 더해줍니다
    print(result)
    # 결과를 출력해줍니다