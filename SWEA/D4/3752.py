TC = int(input())

for T in range(TC):
    N = int(input())
    points = list(map(int, input().split()))
    result = [0]

    for i in range(N):
        result = list(set(result))
        for j in range(len(result)):
            result.append(result[j] + points[i])
    
    print(f'#{T + 1} {len(set(result))}')