n, k = map(int, input().split())
# n, k를 받아줍니다.
coms = []
# 조합을 담을 리스트를 만들어줍니다.
def dfs(num, combination):
    if num > n:
        return
    # 조합의 합이 원하는 범위를 넘어서면 연산을 멈추어줍니다.
    elif num == n:
        coms.append(combination[:-1])
        # 조합의 합이 원하는 값에 도달하였다면 문자열 마지막의 +를 빼고 coms에 문자열을 넣어줍니다.
    for i in range(1, 4):
        dfs(num + i, combination + str(i) + '+')
        # 1, 2, 3을 더하여 조합을 실행시켜줍니다.

dfs(0, '')
if len(coms) < k:
    print(-1)
else:
    print(coms[k - 1])
# 조합의 길이가 k보다 작다면 -1을 출력하여주고
# 조합의 길이가 존재한다면 coms의 인덱스값을 찾아 출력하여줍니다.