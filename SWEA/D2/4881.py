T = int(input())

def backtracing(idx, total):
    global n
    global result

    if idx == n:
        result = min(result, total)
        return 
    
    for line in maps:
        if line[0] == 0:
            total += line[1][idx]
            line[0] = 1
            if total < result:
                backtracing(idx + 1, total)
            total -= line[1][idx]
            line[0] = 0

for tc in range(1, T + 1):
    n = int(input())
    result = n * 10
    maps = [[0, list(map(int, input().split()))] for _ in range(n)]

    backtracing(0, 0)
    print(f'#{tc} {result}')