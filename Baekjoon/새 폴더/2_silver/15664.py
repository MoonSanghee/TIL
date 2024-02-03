n, m = map(int, input().split())
numbers = list(map(int, input().split()))
# 수의 개수와 만들 수열의 길이 주어지는 수열을 받아줍니다.
numbers.sort()
visited = [False] * n
# 수열을 정열하고 사용하였는지 확인할 수열과 길이가 같은 리스트를 만들어줍니다.
com = []
# 만들 수열을 담을 빈 리스트를 만들어줍니다.

def dfs(start):
    if len(com) == m:
        print(*com)
        return
    # 수열의 길이가 충분해졌다면 출력하여줍니다.
    used = 0
    # 이번 연산에서 사용한 수인지 확인해주는 변수를 만들어줍니다.
    for i in range(start, n):
        if not visited[i] and numbers[i] != used:
            # 같은 자리에서 사용된적 없고 방문한 적 없는 수라면
            visited[i] = True
            com.append(numbers[i])
            dfs(i + 1)
            # 방문 처리하고 조합에 수를 넣은 뒤 다음 자리부터 함수를 재귀하도록 합니다.
            used = numbers[i]
            visited[i] = False
            com.pop()
            # 이번 연산에서 사용한 수를 표시해주고 방문을 취소한다음 조합에 들어간 마지막값을 빼줍니다.

dfs(0)
# 0부터 함수를 실행시켜줍니다.