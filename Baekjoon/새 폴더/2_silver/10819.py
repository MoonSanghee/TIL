n = int(input())
numbers = list(map(int, input().split()))
visited = [False] * n
# 수와 수열, 수열에서 수를 사용하였는지 표시해줄 리스트를 만들어줍니다.
result = -1000
# 모든 차를 합한 값은 -100이 8개인 -800보다 크므로 -1000으로 설정해주었습니다.
def dfs(x, num, total):
    global result
    if x == n:
        result = max(result, total)
    # 수열이 완성되었다면 글로벌 result 값과 새로 만든 수열의 합을 비교하여줍니다.
    for i in range(n):
        if not visited[i]:
            if x == 0:
                visited[i] = True
                dfs(x + 1, numbers[i], total)
                visited[i] = False
                # x가 0이라면 비교하여 차를 구할수 없으므로 방문 처리만하고 1개의 수를 뽑았다는 표시와 수를 넘겨 재귀를 실행합니다. 
            else:
                total += abs(num - numbers[i])
                visited[i] = True
                dfs(x + 1, numbers[i], total)
                visited[i] = False
                total -= abs(num - numbers[i])
                # 1부터는 total에 이전 수와의 차의 절대값을 더하여 재귀를 실행시켜줍니다.
dfs(0, 0, 0)
print(result)
# 재귀 함수를 실행시키고 result에 담긴 값을 출력해줍니다.