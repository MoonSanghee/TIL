N = int(input())
K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    if i > (N + 1) / 2:
        i = N + 1 - i
    
    if j > (N + 1) / 2:
        j = N + 1 - j
    
    if i > j:
        answer = j % 3
    else:
        answer = i % 3
    
    if answer == 0:
        answer = 3
    
    print(answer)