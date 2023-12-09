n, k = map(int, input().split())
numbers = list(map(int, input().split()))
# n, k와 수열을 받아줍니다.
result = 0
# n이하의 최대값을 담을 변수를 만들어줍니다.
def dfs(num):
    global result
    if num > n:
        return
    # 함수에 주어진 변수가 n보다 크면 연산을 멈춥니다.
    else:
        result = max(result, num)
    # 아니라면 result값과 num을 비교하여 갱신해줍니다.
    new = num * 10
    for number in numbers:
        dfs(new + number)
    # num값에 10을 곱하고 수열의 수를 더한 값을 넣어 재귀함수를 실행합니다.

dfs(0)
print(result)
# 함수에 0을 넣고 실행하여 받은 결과를 출력해줍니다.