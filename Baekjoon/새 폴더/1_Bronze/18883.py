n, m = map(int, input().split())
# 주어지는 영역의 크기를 받아줍니다
line = [i + 1 for i in range(m)]
# 첫 줄의 출력을 담을 리스트를 만들어줍니다
for i in range(n):
    print(*line)
    for j in range(m):
        line[j] += m
    # 출력해야하는 줄의 수만큼 반복하며 이전 저장된 줄을 출력하고 줄의 모든 값을 m만큼 더해줍니다