n, k = map(int, input().split())
A = list(map(int, input().split()))
# 기구의 수와 하루 근손실을 받고 기구의 효과를 받아줍니다.
used = [False] * n
result = 0
# 기구를 사용했는지 확인할 변수를 설정하고 중량을 유지할수있는 경우의 수가 몇개인지 담을 변수를 설정해줍니다.
def check(days, weight):
    global result
    if weight < 0:
        return
    # 주어지는 기준 중량 아래로 내려가면 확인을 멈추어줍니다.
    if days == n:
        result += 1
        return
    # n일이 지나면 경우의 수를 1늘려줍니다.
    weight -= k
    # 하루 근손실을 적용해줍니다.
    for i in range(n):
        if not used[i]:
            used[i] = True
            check(days + 1,weight + A[i])
            used[i] = False
            # 사용하지 않은 기구를 확인하여 사용하도록 재귀하며 모든 기구를 사용할때까지 시행해줍니다

check(0, 0)
# 기준이 500이지만 0으로 시작해 0아래로 떨어지지 않으면 같은 결과가 나오므로 0,0으로 함수를 실행해줍니다.
print(result)
# 경우의 수가 몇개인지 출력해줍니다.