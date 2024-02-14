n = int(input())
dp = [1, 1, 0, 1, 1]
# dp리스트에 돌의 개수와 5개까지의 상근이가 이길 수 있는 경우 1, 지는 경우 0을 넣어줍니다.
for i in range(5,n + 1):   
        if dp[i - 1] + dp[i - 3] + dp[i - 4] == 3 :
            dp.append(0)
        else :
            dp.append(1)
# 이후부터는 상근이가 질 수 밖에 없으면 0을 넣고 아니면 1을 넣어줍니다.
if dp[n] == 1 :
    print("SK")
else :
    print("CY")
    # n번째 돌을 가져갈때 누가 이기는지 확인하고 결과를 출력해줍니다.