num = int(input())
# 정수를 받아줍니다.
dp = [0] * 68
# 입력받는 가장 큰 값이 67이므로 67번 인덱스까지 받기위해 
# 68개의 0을 가지는 리스트를 만들어줍니다.
def koong(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if dp[n]:
        return dp[n]
    dp[n] = koong(n-1) + koong(n-2) + koong(n-3) + koong(n-4)
    return dp[n]
# koong함수를 주어진 조건에 따라 정의해줍니다.
for _ in range(num):
    number = int(input())
    print(koong(number))
    # 입력받은 정수에 따라 함수를 실행시킨 결과를 출력해줍니다.