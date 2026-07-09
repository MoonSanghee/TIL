T = int(input())
# 테스트케이스의 개수를 받아줍니다
for tc in range(T):
    N, L = map(int, input().split())
    infomation = [list(map(int, input().split())) for _ in range(N)]
    # 주어지는 변수들을 받아줍니다
    dp = [0] * (L + 1)
    # L + 1길이의 dp리스트를 만들어줍니다
    for t, k in infomation:
        for i in range(L, k - 1, -1):
            dp[i] = max(dp[i], dp[i - k] + t)
    # 각 재료 정보를 순회하며 재료를 사용하였을때 최고 효율을 확인해줍니다
    print(f'#{tc + 1} {dp[-1]}')
    # 결과를 주어진 양식에 맞게 출력해줍니다