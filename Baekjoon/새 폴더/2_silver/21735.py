n, m = map(int, input().split())
field = list(map(int, input().split()))
result = 0
# 영역의 크기와 주어지는 시간, 눈이 쌓여있는 상태를 받고 결과를 담을 변수를 설정해줍니다
def dfs(idx, time, size):
    global result
    size += field[idx]
    if time == m or idx == n - 1:
        result = max(result, size)
        return
    # 시간을 다 썼거나 영역을 다 썼다면 크기를 비교해 갱신해줍니다
    if idx + 1 < n:
        dfs(idx + 1, time + 1, size)
    if idx + 2 < n:
        dfs(idx + 2, time + 1, size // 2)
    # 영역안에서 더 굴리거나 던질수있다면 재귀를 실행해줍니다

dfs(0, 1, 1)
if n > 1:
    dfs(1, 1, 0)
# 굴려서 시작하는 경우와 던져서 시작하는 경우로 함수를 실행해줍니다
print(result)
# 결과값을 출력해줍니다