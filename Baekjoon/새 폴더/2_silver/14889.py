n = int(input())
# 사람의 수를 받아줍니다.

maps = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
result = 10000
# 각 조합의 시너지와 방문처리를 해 줄 리스트를 만들어줍니다.
# 결과에 10000을 넣어줍니다. (조합으로 나올 최대 100이고 10명일때 45가지 조합을 각
# 100개 1개를 가지면 4500이 되므로 그보다 큰 수를 넣어주었습니다.)

def com(l, x):
    global result
    if l == n // 2:
        # 절반의 팀을 뽑았다면 
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                if visited[i] and visited[j]:
                    power1 += maps[i][j] + maps[j][i]
                elif not visited[i] and not visited[j]:
                    power2 += maps[i][j] + maps[j][i]
        result = min(result, abs(power1 - power2))
        # 두 명이 모두 뽑힌 사람일때 power1에 두 명 모두 안 뽑힌 사람이면 power2에
        # 조합에서 나오는 시너지를 더해줍니다.
        # global에 저장된 result와 power1과 power2를 비교해 작은값으로 갱신해줍니다. 
        return
    for i in range(x, n):
        if not visited[i]:
            visited[x] = 1
            com(l + 1, i + 1)
            visited[x] = 0
            # x부터 n사이에 뽑은적 없다면 뽑았다고 표시해주고 
            # 뽑은 사람을 1명 추가하고 확인할 자리를 1자리 뒤로 한 다음 함수를 시행해주고
            # 방문을 취소해줍니다.
com(0, 0)
# 조합을 만들고 차이를 확인하는 함수를 시행해줍니다.
print(result)
# result에 저장된 값을 출력해줍니다.