n = int(input())
dp = [1]
# 정수를 받고 0번 인덱스 값으로 1을 넣은 dp리스트를 만들어줍니다.
while True:
    if len(dp) == n + 1:
        break
    # dp리스트의 길이가 충분하면 연산을 멈추어줍니다.
    result = 0
    # 점화식을 실행시키고 dp에 추가시킬 값을 구할 result을 선언해줍니다.
    for i in range(len(dp)):
        result += dp[i] * dp[len(dp) - i - 1]
    dp.append(result)
    # 점화식을 계산하여 구한 result 값을 dp리스트에 넣어줍니다.
    
print(dp[-1])
# dp리스트의 마지막 값을 출력해줍니다.