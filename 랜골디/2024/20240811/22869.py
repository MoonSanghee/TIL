n, k = map(int, input().split())
stones = list(map(int, input().split()))
# 돌의 개수와 최대 힘의 크기를 받고 돌이 놓여진 상태를 받아줍니다.
visited = [False for _ in range(n)]
visited[0] = True
# 각 돌에 도달할수 있는지 확인하기위한 visited 리스트를 만들고 첫 돌을 방문처리해줍니다.
for i in range(n):
    if visited[i] == True:
        for j in range(i + 1, n):
            if (j - i) * (1 + (abs(stones[i] - stones[j]))) <= k:
                visited[j] = True
# 모든 돌을 순회하면서 방문한 돌이라면 이후의 돌들로 이동할 수 있는지 확인해줍니다.
if visited[-1]:
    print("YES")
else:
    print("NO")
# 마지막 돌에 이동할수 있는지를 확인하여 결과를 출력해줍니다.