import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
visited = [False for _ in range(N + 1)]
# 주어지는 땅의 수와 오리의 수를 받고 점유된 땅을 표시할 리스트를 만들어줍니다
for _ in range(Q):
    x = int(input())
    target = x
    block = 0
    # 점유하려는 땅의 번호를 받고 값을 복사해둔 뒤 막히는 경로가 있는지 확인해줍니다
    while x:
        if visited[x]:
            block = x
        x //= 2
        # 트리를 거슬러 올라가며 이미 점유된 땅이 있다면 값을 갱신해줍니다
    if block:
        print(block)
    else:
        print(0)
        visited[target] = True
        # 막힌적 있다면 가장 앞에서 막힌 위치를 아니라면 0을 출력하고 점유를 표시해줍니다