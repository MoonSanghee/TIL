T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    n, m = map(int, input().split())
    dp = [0] * (n + 1)
    # 주어지는 변수들을 받고 dp 리스트를 만들어줍니다
    for _ in range(m):
        s, p = map(int, input().split())
        # 물건의 크기와 가격을 받아줍니다
        for i in range(n , s - 1, -1):
            dp[i] = max(dp[i], dp[i - s] + p)
        # 중복 사용을 방지하기위해 상자를 담을수있는 최대 크기부터 역순으로 확인하며 최대 가격을 갱신해줍니다
    print(f'#{t + 1} {dp[-1]}')
    # 결과를 출력해줍니다