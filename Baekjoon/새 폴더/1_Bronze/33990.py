n = int(input())
# 
result = 601
for _ in range(n):
    total = sum(list(map(int, input().split())))
    if total >= 512:
        result = min(result, total)

if result == 601:
    print(-1)
else:
    print(result)