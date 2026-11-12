T = int(input())

def dfs(s, idx):
    global result
    if idx == n:
        return
    if len(s.union(words[idx])) == 26:
        result += 1
    
    dfs(s.union(words[idx]), idx + 1)
    dfs(s, idx + 1)

for tc in range(1, T + 1):
    n = int(input())
    result = 0

    words = [set(input().strip()) for _ in range(n)]
    
    dfs(set(),0)

    print(f'#{tc} {result}')